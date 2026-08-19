import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------

st.set_page_config(
    page_title="Dashboard Epidemiológico COVID-19",
    page_icon=":bar_chart:",
)

# ----------------------------
# CONSTANTES
# -----------------------------

COLUMNAS_REQUERIDAS = [
    "País",
    "Confirmados",
    "Muertes",
    "Recuperaciones",
    "Activos",
    "Nuevos Casos",
    "Nuevas Muertes",
    "Nuevas Recuperaciones",
    "Muertes / 100 Casos",
    "Recuperaciones / 100 Casos",
    "Muertes / 100 Recuperaciones",
    "Confirmados Última Semana",
    "Cambio 1 Semana",
    "% Incremento 1 Semana",
    "Región OPS",
]

COLUMNAS_NUMERICAS = [
    "Confirmados",
    "Muertes",
    "Recuperaciones",
    "Activos",
    "Nuevos Casos",
    "Nuevas Muertes",
    "Nuevas Recuperaciones",
    "Muertes / 100 Casos",
    "Recuperaciones / 100 Casos",
    "Muertes / 100 Recuperaciones",
    "Confirmados Última Semana",
    "Cambio 1 Semana",
    "% Incremento 1 Semana",
]

COLUMNAS_FECHAS = []

# ----------------------------
# FUNCIONES
# ----------------------------

# Nota aclaratoria:
#
# La nomenclatura
#
#   nombre_funcion(param: tipo) -> tipo_de_retorno
#
# establece el tipo de dato que se espera recibir y retornar al culminar la ejecución
# de la función. Esto es útil para la documentación y para el autocompletado en IDEs.


def validar_columnas(df: pd.DataFrame) -> bool:
    """
    Valida que el DataFrame contenga todas las columnas requeridas.

    Args:
        df (pd.DataFrame): DataFrame a validar.

    Returns:
        bool: True si todas las columnas requeridas están presentes, False en caso contrario.
    """
    columnas_faltantes = [col for col in COLUMNAS_REQUERIDAS if col not in df.columns]
    if columnas_faltantes:
        return False, columnas_faltantes

    return True, []


def preparar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepara el DataFrame para su análisis y visualización.

    Args:
        df (pd.DataFrame): DataFrame original con los datos.

    Returns:
        pd.DataFrame: DataFrame preparado con las columnas requeridas y tipos de datos correctos.
    """
    df = df.copy()

    # Eliminar espacios en los nombres de las columnas
    df.columns = df.columns.astype(str).str.strip()

    # Convertir variables numéricas y rellenar valores faltantes con 0
    for col in COLUMNAS_NUMERICAS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Convertir variables de fecha
    for col in COLUMNAS_FECHAS:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").fillna(
                pd.Timestamp("1970-01-01")
            )

    return df


# ----------------------------
# CARGA DEL ARCHIVO DE DATOS
# ----------------------------

st.sidebar.header("📂 Fuente de datos")

archivo = st.sidebar.file_uploader("Selecciona un archivo XLSX", type=["xlsx"])

if archivo is None:
    st.info("Carga un archivo XLSX para comenzar el análisis.")

    st.markdown("""
        ### Estructura esperada

        El archivo debe contener como mínimo las siguientes columnas:
        - País
        - Confirmados
        - Muertes
        - Recuperaciones
        - Activos
        - Nuevos Casos
        - Nuevas Muertes
        - Nuevas Recuperaciones
        - Muertes / 100 Casos
        - Recuperaciones / 100 Casos
        - Muertes / 100 Recuperaciones
        - Confirmados Última Semana
        - Cambio 1 Semana
        - % Incremento 1 Semana
        - Región OPS
        """)

    st.stop()

# ----------------------------
# LECTURA DEL ARCHIVO
# ----------------------------

# Nota aclaratoria:
#
# Se utiliza un bloque try-except para manejar posibles errores al leer el archivo XLSX.
# En caso de que ocurra un error, se puede mostrar un mensaje adecuado al usuario.

try:
    df = pd.read_excel(archivo, engine="openpyxl")
except Exception as error:
    st.error(f"Error al leer el archivo XLSX: {error}")
    st.stop()

# ----------------------------
# VALIDACIÓN Y PREPARACIÓN DEL ARCHIVO
# ----------------------------

columnas_validas, columnas_faltantes = validar_columnas(df)

if not columnas_validas:
    st.error(
        f"Faltan las siguientes columnas requeridas: {', '.join(columnas_faltantes)}"
    )
    st.stop()

df = preparar_datos(df)

# ----------------------------
# FILTROS
# ----------------------------

st.sidebar.header("🔍 Filtros")

if "Región OPS" in df.columns:
    regiones = df["Región OPS"].dropna().unique().tolist()

    regiones_seleccionadas = st.sidebar.multiselect(
        "Región OPS", options=regiones, default=regiones
    )

    df_filtrado = df[df["Región OPS"].astype(str).isin(regiones_seleccionadas)].copy()

else:
    df_filtrado = df.copy()

if "País" in df.columns:
    paises = ["Todos"] + df["País"].dropna().unique().tolist()

    pais_seleccionado = st.sidebar.selectbox(
        "País", options=paises, index=paises.index("Todos")
    )

    if pais_seleccionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["País"] == pais_seleccionado].copy()

# ----------------------------
# RESUMEN DE DATOS
# ----------------------------

resumen = {
    "Confirmados": df_filtrado["Confirmados"].sum(),
    "Activos": df_filtrado["Activos"].sum(),
    "Recuperaciones": df_filtrado["Recuperaciones"].sum(),
    "Muertes": df_filtrado["Muertes"].sum(),
    "Nuevos Casos": df_filtrado["Nuevos Casos"].sum(),
    "Nuevas Muertes": df_filtrado["Nuevas Muertes"].sum(),
    "Nuevas Recuperaciones": df_filtrado["Nuevas Recuperaciones"].sum(),
}

# ----------------------------
# KPIs
# ----------------------------

if df_filtrado.empty:
    st.warning("No hay datos disponibles para los filtros seleccionados.")
    st.stop()

st.subheader("📊 Indicadores principales")

# Primera Fila

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Casos Confirmados", "{:,}".format(resumen["Confirmados"]))
with c2:
    st.metric("Casos Activos", "{:,}".format(resumen["Activos"]))
with c3:
    st.metric("Recuperaciones", "{:,}".format(resumen["Recuperaciones"]))
with c4:
    st.metric("Muertes", "{:,}".format(resumen["Muertes"]))

# Segunda Fila

c5, c6, c7, c8 = st.columns(4)

confirmados = resumen["Confirmados"]
activos = resumen["Activos"]
recuperaciones = resumen["Recuperaciones"]
muertes = resumen["Muertes"]

pct_letalidad = (muertes / confirmados * 100) if confirmados > 0 else 0
pct_activos = (activos / confirmados * 100) if confirmados > 0 else 0
pct_recuperaciones = (recuperaciones / confirmados * 100) if confirmados > 0 else 0

with c5:
    st.metric("Nuevos Casos", "{:,}".format(resumen["Nuevos Casos"]))
with c6:
    st.metric("Nuevas Muertes", "{:,}".format(resumen["Nuevas Muertes"]))
with c7:
    st.metric("Letalidad Acumulada", f"{pct_letalidad:.2f}%")
with c8:
    st.metric("Casos Activos (%)", "{:.2f}%".format(pct_activos))

# ----------------------------
# TABS
# ----------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    ["🌎 Países", "🗺️ Regiones OPS", "⚠️ Riesgo", "📋 Datos"]
)

# TAB 1: Países

with tab1:
    st.subheader("Comparación entre Países")

    resumen_pais = (
        df_filtrado.groupby("País")
        .agg(
            {
                "Confirmados": "max",
                "Activos": "max",
                "Recuperaciones": "max",
                "Muertes": "max",
                "Nuevos Casos": "sum",
                "Nuevas Muertes": "sum",
                "% Incremento 1 Semana": "mean",
            }
        )
        .reset_index()
    )

    resumen_pais["Letalidad (%)"] = (
        resumen_pais["Muertes"] / resumen_pais["Confirmados"] * 100
    ).round(2)

    col1, col2 = st.columns(2)

    with col1:
        top_casos = resumen_pais.sort_values(by="Confirmados", ascending=False).head(10)
        fig1 = px.bar(
            top_casos,
            x="Confirmados",
            y="País",
            orientation="h",
            title="Top 10 Países por Casos Confirmados",
            color="Confirmados",
            color_continuous_scale="Blues",
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        top_activos = resumen_pais.sort_values(by="Activos", ascending=False).head(10)
        fig2 = px.bar(
            top_activos,
            x="Activos",
            y="País",
            orientation="h",
            title="Top 10 Países por Casos Activos",
            color="Activos",
            color_continuous_scale="Oranges",
        )
        st.plotly_chart(fig2, use_container_width=True)

    crecimiento = resumen_pais.sort_values(
        by="% Incremento 1 Semana", ascending=False
    ).head(10)
    fig3 = px.bar(
        crecimiento,
        x="% Incremento 1 Semana",
        y="País",
        orientation="h",
        title="Top 10 Países por Incremento Semanal",
        color="% Incremento 1 Semana",
        color_continuous_scale="Reds",
    )
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.scatter(
        resumen_pais,
        x="% Incremento 1 Semana",
        y="Letalidad (%)",
        color="Activos",
        size="Confirmados",
        hover_name="País",
        title="Relación entre Incremento Semanal y Letalidad",
        labels={
            "% Incremento 1 Semana": "Incremento Semanal (%)",
            "Letalidad (%)": "Letalidad (%)",
            "Activos": "Casos Activos",
            "Confirmados": "Casos Confirmados",
        },
        color_continuous_scale="Reds",
    )
    st.plotly_chart(fig4, use_container_width=True)

# TAB 2: Regiones OPS

with tab2:
    st.subheader("Comparación entre Regiones OPS")

    resumen_region = (
        df.groupby("Región OPS")
        .agg(
            {
                "Confirmados": "max",
                "Activos": "max",
                "Recuperaciones": "max",
                "Muertes": "max",
                "Nuevos Casos": "sum",
                "Nuevas Muertes": "sum",
            }
        )
        .reset_index()
    )

    resumen_region["Letalidad (%)"] = (
        resumen_region["Muertes"] / resumen_region["Confirmados"] * 100
    ).round(2)

    col1, col2 = st.columns(2)

    with col1:
        fig5 = px.pie(
            resumen_region,
            names="Región OPS",
            values="Confirmados",
            title="Distribución de Casos Confirmados por Región OPS",
        )
        st.plotly_chart(fig5, use_container_width=True)

    with col2:
        fig6 = px.bar(
            resumen_region.sort_values(by="Activos", ascending=False),
            x="Región OPS",
            y="Activos",
            orientation="v",
            title="Casos Activos por Región OPS",
            color="Activos",
            color_continuous_scale="Oranges",
        )
        st.plotly_chart(fig6, use_container_width=True)

    fig7 = px.bar(
        resumen_region.sort_values(by="Letalidad (%)", ascending=False),
        x="Región OPS",
        y="Letalidad (%)",
        orientation="v",
        title="Letalidad por Región OPS",
        color="Letalidad (%)",
        color_continuous_scale="Reds",
    )
    st.plotly_chart(fig7, use_container_width=True)

# TAB 3: Riesgo

with tab3:
    st.subheader("Priorización de Países por Nivel de Riesgo")

    riesgo = (
        df_filtrado.groupby("País")
        .agg(
            {
                "Confirmados": "max",
                "Activos": "max",
                "% Incremento 1 Semana": "mean",
                "Nuevos Casos": "sum",
                "Nuevas Muertes": "sum",
            }
        )
        .reset_index()
    )

    crecimiento = riesgo["% Incremento 1 Semana"] / 100

    riesgo["Riesgo"] = (
        (riesgo["Activos"] / riesgo["Confirmados"]) * 0.4
        + (crecimiento) * 0.3
        + (riesgo["Nuevos Casos"] / riesgo["Confirmados"]) * 0.2
        + (riesgo["Nuevas Muertes"] / riesgo["Confirmados"]) * 0.1
    )

    riesgo = riesgo.sort_values(by="Riesgo", ascending=False).head(10)

    fig8 = px.bar(
        riesgo,
        x="Riesgo",
        y="País",
        orientation="h",
        color="Riesgo",
        color_continuous_scale="Reds",
        title="Top Países por Nivel de Riesgo",
    )
    st.plotly_chart(fig8, use_container_width=True)


# TAB 4: Datos

with tab4:
    st.subheader("Datos Procesados")

    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)

    csv = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Descargar CSV",
        data=csv,
        file_name="datos_procesados.csv",
        mime="text/csv",
    )

# ----------------------------
# PIE DE PÁGINA
# ----------------------------

st.divider()

st.caption(
    "Dashboard Epidemiológico COVID-19 - Fuente: Organización Panamericana de la Salud (OPS)"
)
