import pandas as pd
import plotly.express as px
import streamlit as st


def limpiar_filtros():
    """
    Restablece los filtros de la barra lateral a sus valores predeterminados.
    """
    st.session_state["fecha_inicio"] = pd.to_datetime(df["Fecha"].min())
    st.session_state["fecha_fin"] = pd.to_datetime(df["Fecha"].max())
    st.session_state["clasificaciones"] = ["Todos"]
    st.session_state["rama"] = ["Todos"]
    st.session_state["ciudades"] = df["Ciudad"].unique().tolist()
    st.session_state["id_venta"] = ""


# Configurar la página de Streamlit
st.set_page_config(
    page_title="Dashboard de Ventas", layout="wide", initial_sidebar_state="expanded"
)

# Cargar los datos del archivo CSV
df = pd.read_csv("supermercado.csv")
df_filtrado = (
    df.copy()
)  # Crear una copia del DataFrame original para aplicar los filtros

st.title("Ventas")

# --------------------
# Sidebar - Filtros
# --------------------

st.sidebar.title("Filtros")

fecha_inicio = st.sidebar.date_input(
    "Fecha de inicio", value=pd.to_datetime(df["Fecha"].min()), key="fecha_inicio"
)
fecha_fin = st.sidebar.date_input(
    "Fecha de fin", value=pd.to_datetime(df["Fecha"].max()), key="fecha_fin"
)

clasificaciones = df["ClasificacionProducto"].unique().tolist()
clasificacion_seleccionada = st.sidebar.selectbox(
    "Seleccione las clasificaciones de producto",
    options=["Todos"] + clasificaciones,
    key="clasificaciones",
)

ramas = df["Rama"].unique().tolist()
rama_seleccionada = st.sidebar.selectbox(
    "Seleccione la rama de venta", options=["Todos"] + ramas, key="rama"
)

ciudades = df["Ciudad"].unique().tolist()
ciudades_seleccionadas = st.sidebar.multiselect(
    "Seleccione las ciudades de venta",
    options=ciudades,
    default=ciudades,
    key="ciudades",
)

st.sidebar.divider()
st.sidebar.button("Limpiar filtros", on_click=limpiar_filtros, key="limpiar_filtros")

# --------------------
# Búsqueda por ID de venta
# --------------------

st.subheader("Búsqueda")
id_venta = st.text_input("Ingrese el ID de la venta que desea buscar:", key="id_venta")

# --------------------
# Filtrado de datos
# --------------------

# Nota importante:
#
# Los filtros se aplican en el orden en que se definen,
# por lo que el filtro por ID de venta se aplica primero, seguido por los filtros de fecha,
# clasificación, rama y ciudades.
# Resulta importante tener en cuenta que estos controladores deben definirse antes de calcular
# las métricas clave y realizar el análisis visual, ya que los resultados de estos cálculos
# dependen del DataFrame filtrado.

# Controlador de filtro por ID de venta
df_filtrado = (
    df_filtrado[df_filtrado["IDFactura"] == id_venta] if id_venta else df_filtrado
)


# Controlador de filtro por rango de fechas
df["Fecha"] = pd.to_datetime(df["Fecha"])
df_filtrado = (
    df[
        (
            (df["Fecha"] >= pd.to_datetime(fecha_inicio))
            & (df["Fecha"] <= pd.to_datetime(fecha_fin))
        )
    ]
    if fecha_inicio and fecha_fin
    else df
)

# Controlador de filtro por clasificación de producto
df_filtrado = (
    df_filtrado[df_filtrado["ClasificacionProducto"] == clasificacion_seleccionada]
    if clasificacion_seleccionada and clasificacion_seleccionada != "Todos"
    else df_filtrado
)

# Controlador de filtro por rama de venta
df_filtrado = (
    df_filtrado[df_filtrado["Rama"] == rama_seleccionada]
    if rama_seleccionada and rama_seleccionada != "Todos"
    else df_filtrado
)

# Controlador de filtro por ciudades
df_filtrado = (
    df_filtrado[df_filtrado["Ciudad"].isin(ciudades_seleccionadas)]
    if ciudades_seleccionadas
    else df_filtrado
)

# --------------------
# Métricas clave
# --------------------

# Nota importante:
#
# Las métricas clave se calculan utilizando fórmulas aritméticas simples, propias de la estadística,
# como sumas y promedios. Esto implica que el analista debe tener conocimientos básicos de estadística
# aplicada a su área de trabajo para poder definir correctamente las métricas que desea calcular.
# Se puede utilizar IA para apoyar la definición de métricas, pero es importante que el analista
# comprenda los conceptos estadísticos subyacentes.
# Un ejemplo de prompt se encuentra en el archivo "prompt_metrica.txt" y se puede utilizar para generar métricas
# clave para distintas áreas de trabajo.

st.subheader("Resumen General")

col1, col2, col3, col4 = st.columns(4)

col1.metric(label="Ingresos Totales", value=f"$ {df_filtrado['MontoVenta'].sum():,.2f}")
col2.metric(
    label="Ganacia Neta Total", value=f"$ {df_filtrado['GananciaNeta'].sum():,.2f}"
)
col3.metric(
    label="Margen de Ganancia Neto (%)",
    value=f"{(df_filtrado['GananciaNeta'].sum() / df_filtrado['MontoVenta'].sum()) * 100:.2f}%",
)
col4.metric(
    label="Costo Total de Ventas (COGS)", value=f"$ {df_filtrado['Costo'].sum():,.2f}"
)

col5, col6, col7 = st.columns(3)

col5.metric(
    label="Ticket Promedio",
    value=f"$ {df_filtrado['MontoVenta'].sum() / df_filtrado['IDFactura'].nunique():,.2f}",
)
col6.metric(label="Unidades Vendidas", value=f"{df_filtrado['Cantidad'].sum():,.0f}")
col7.metric(
    label="Unidades por Ticket",
    value=f"{df_filtrado['Cantidad'].sum() / df_filtrado['IDFactura'].nunique():,.2f}",
)

# --------------------
# Análisis visual
# --------------------

st.subheader("Análisis Visual")

# Markdown es un lenguaje de marcado ligero que permite dar formato al texto de manera sencilla.
# En este caso, se utiliza para resaltar el título de la sección de ventas por clasificación de producto.
# Algunos estilos que podemos manejar con markdown son:
# - **Negrita**: Se utiliza para resaltar palabras o frases importantes.
# - *Cursiva*: Se utiliza para enfatizar palabras o frases.
# - `Código`: Se utiliza para resaltar fragmentos de código o comandos.
# - Listas: Se pueden crear listas ordenadas o desordenadas para organizar información.
st.markdown("**Ventas por clasificación de producto**")

# El proceso de creación de gráficos con Plotly Express implica tres pasos principales:
# 1. Preparar los datos: Un DataFrame de Pandas que contiene la información que se desea visualizar.
# 2. Crear el gráfico: Utilizando la función correspondiente de Plotly Express (en este caso, px.bar
#    para generar un gráfico de barras).
# 3. Anexar el gráfico a la aplicación Streamlit: Utilizando st.plotly_chart para mostrar el gráfico en la interfaz de usuario.

ventas_por_clasificacion = (
    df_filtrado.groupby("ClasificacionProducto")["MontoVenta"]
    .sum()
    .reset_index()
    .sort_values(by="MontoVenta", ascending=True)
)
fig_bar = px.bar(
    ventas_por_clasificacion,
    x="MontoVenta",
    y="ClasificacionProducto",
    orientation="h",
)
st.plotly_chart(fig_bar, use_container_width=True)

# --------------------
# Dataframe filtrado
# --------------------

st.divider()
st.dataframe(df_filtrado)
