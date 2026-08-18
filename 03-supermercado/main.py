# -------------------------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# -------------------------------------------------------------------
# Pandas nos ayuda a trabajar con datos en forma de tablas (DataFrames).
# Plotly Express nos permite crear gráficos interactivos de forma sencilla.
# Streamlit construye la interfaz web que estamos viendo en el navegador.
import pandas as pd
import plotly.express as px
import streamlit as st


def limpiar_filtros():
    """
    Restablece los filtros de la barra lateral a sus valores originales.

    Esta función se ejecuta cuando el usuario hace clic en el botón
    "Limpiar filtros". Simplemente devuelve cada filtro a su valor
    por defecto usando la sesión de Streamlit (st.session_state).
    """
    st.session_state["fecha_inicio"] = pd.to_datetime(df["Fecha"].min())
    st.session_state["fecha_fin"] = pd.to_datetime(df["Fecha"].max())
    st.session_state["clasificaciones"] = ["Todos"]
    st.session_state["rama"] = ["Todos"]
    st.session_state["ciudades"] = df["Ciudad"].unique().tolist()
    st.session_state["id_venta"] = ""


# -------------------------------------------------------------------
# CONFIGURACIÓN INICIAL DE LA PÁGINA
# -------------------------------------------------------------------
# Le decimos a Streamlit cómo queremos que se vea nuestra aplicación:
# un título para la pestaña del navegador, un diseño ancho y la barra
# lateral expandida (visible desde el inicio).
st.set_page_config(
    page_title="Dashboard de Ventas", layout="wide", initial_sidebar_state="expanded"
)

# -------------------------------------------------------------------
# CARGA DE DATOS
# -------------------------------------------------------------------
# Leemos el archivo CSV con pandas y lo guardamos en un DataFrame.
# Un DataFrame es como una hoja de cálculo: tiene filas y columnas.
df = pd.read_csv("supermercado.csv")

# Hacemos una copia del DataFrame original. Esto es importante porque
# después iremos aplicando filtros (como fechas, ciudades, etc.) y no
# queremos perder los datos originales. Trabajaremos sobre la copia.
df_filtrado = df.copy()

# Título principal de nuestra aplicación
st.title("Ventas")

# -------------------------------------------------------------------
# BARRA LATERAL (SIDEBAR) - FILTROS
# -------------------------------------------------------------------
# La barra lateral es el panel que aparece a la izquierda.
# Aquí el usuario puede elegir qué datos quiere ver.

st.sidebar.title("Filtros")

# ---- Filtro por rango de fechas ----
# El usuario elige una fecha de inicio y una fecha de fin.
# Solo se mostrarán las ventas que estén dentro de ese período.
fecha_inicio = st.sidebar.date_input(
    "Fecha de inicio", value=pd.to_datetime(df["Fecha"].min()), key="fecha_inicio"
)
fecha_fin = st.sidebar.date_input(
    "Fecha de fin", value=pd.to_datetime(df["Fecha"].max()), key="fecha_fin"
)

# ---- Filtro por clasificación de producto ----
# Obtenemos todas las clasificaciones distintas que existen en los datos
# y las mostramos en un menú desplegable (selectbox).
# La opción "Todos" permite no aplicar ningún filtro.
clasificaciones = df["ClasificacionProducto"].unique().tolist()
clasificacion_seleccionada = st.sidebar.selectbox(
    "Seleccione las clasificaciones de producto",
    options=["Todos"] + clasificaciones,
    key="clasificaciones",
)

# ---- Filtro por rama de venta ----
# Similar al anterior, pero para filtrar por la rama o categoría de venta.
ramas = df["Rama"].unique().tolist()
rama_seleccionada = st.sidebar.selectbox(
    "Seleccione la rama de venta", options=["Todos"] + ramas, key="rama"
)

# ---- Filtro por ciudades ----
# A diferencia de los anteriores, aquí podemos seleccionar VARIAS ciudades
# a la vez gracias al multiselect.
ciudades = df["Ciudad"].unique().tolist()
ciudades_seleccionadas = st.sidebar.multiselect(
    "Seleccione las ciudades de venta",
    options=ciudades,
    default=ciudades,  # Por defecto, se muestran todas las ciudades
    key="ciudades",
)

# ---- Botón para limpiar todos los filtros ----
st.sidebar.divider()
st.sidebar.button("Limpiar filtros", on_click=limpiar_filtros, key="limpiar_filtros")

# -------------------------------------------------------------------
# BÚSQUEDA POR ID DE VENTA
# -------------------------------------------------------------------
# Si el usuario conoce el número de factura (ID) de una venta específica,
# puede escribir aquí para encontrar solo esa venta.
st.subheader("Búsqueda")
id_venta = st.text_input("Ingrese el ID de la venta que desea buscar:", key="id_venta")

# -------------------------------------------------------------------
# APLICACIÓN DE FILTROS
# -------------------------------------------------------------------
# Aquí comenzamos a filtrar los datos según lo que el usuario eligió
# en la barra lateral. Es importante que estos filtros se apliquen
# ANTES de calcular las métricas y los gráficos, porque todo lo que
# mostramos después depende de estos datos ya filtrados.
#
# El orden de los filtros importa: primero filtramos por ID de venta,
# luego por fechas, clasificación, rama y finalmente ciudades.

# ---- Filtro 1: por ID de venta ----
# Si el usuario escribió un ID, nos quedamos solo con esa fila.
# Si no escribió nada (id_venta está vacío), mostramos todo.
df_filtrado = (
    df_filtrado[df_filtrado["IDFactura"] == id_venta] if id_venta else df_filtrado
)

# ---- Filtro 2: por rango de fechas ----
# Convertimos la columna "Fecha" a formato de fecha (datetime) para
# poder comparar correctamente. Luego nos quedamos solo con las filas
# cuya fecha esté entre la fecha de inicio y la fecha de fin elegidas.
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

# ---- Filtro 3: por clasificación de producto ----
# Si el usuario eligió una clasificación específica (distinta de "Todos"),
# filtramos para quedarnos solo con los productos de esa clasificación.
df_filtrado = (
    df_filtrado[df_filtrado["ClasificacionProducto"] == clasificacion_seleccionada]
    if clasificacion_seleccionada and clasificacion_seleccionada != "Todos"
    else df_filtrado
)

# ---- Filtro 4: por rama de venta ----
# Misma idea: si se seleccionó una rama específica, filtramos.
df_filtrado = (
    df_filtrado[df_filtrado["Rama"] == rama_seleccionada]
    if rama_seleccionada and rama_seleccionada != "Todos"
    else df_filtrado
)

# ---- Filtro 5: por ciudades ----
# Aquí usamos .isin() porque el usuario pudo haber seleccionado
# varias ciudades. Nos quedamos con las filas cuya ciudad esté
# dentro de la lista de ciudades seleccionadas.
df_filtrado = (
    df_filtrado[df_filtrado["Ciudad"].isin(ciudades_seleccionadas)]
    if ciudades_seleccionadas
    else df_filtrado
)

# -------------------------------------------------------------------
# MÉTRICAS CLAVE (KPI)
# -------------------------------------------------------------------
# Aquí calculamos indicadores importantes del negocio usando operaciones
# básicas como sumas y promedios. Estos números nos dan un resumen
# rápido de cómo van las ventas.
#
# Si quieres crear tus propias métricas, en el archivo
# "prompt_metrica.txt" hay un ejemplo de cómo pedirle ayuda a la IA
# para definirlas. ¡Pero siempre es bueno entender qué significa cada
# número!

st.subheader("Resumen General")

# Organizamos las métricas en columnas para que se vean ordenadas.
# st.columns(4) crea 4 espacios horizontales.
col1, col2, col3, col4 = st.columns(4)

# Ingresos Totales: sumamos todo lo que se vendió (MontoVenta)
col1.metric(label="Ingresos Totales", value=f"$ {df_filtrado['MontoVenta'].sum():,.2f}")
# Ganancia Neta Total: lo que realmente ganamos (Ingresos - Costos)
col2.metric(
    label="Ganacia Neta Total", value=f"$ {df_filtrado['GananciaNeta'].sum():,.2f}"
)
# Margen de Ganancia: qué porcentaje de los ingresos es ganancia neta
col3.metric(
    label="Margen de Ganancia Neto (%)",
    value=f"{(df_filtrado['GananciaNeta'].sum() / df_filtrado['MontoVenta'].sum()) * 100:.2f}%",
)
# COGS (Cost of Goods Sold): el costo total de los productos vendidos
col4.metric(
    label="Costo Total de Ventas (COGS)", value=f"$ {df_filtrado['Costo'].sum():,.2f}"
)

# Otra fila de métricas, ahora en 3 columnas
col5, col6, col7 = st.columns(3)

# Ticket Promedio: cuánto gasta en promedio un cliente por factura
col5.metric(
    label="Ticket Promedio",
    value=f"$ {df_filtrado['MontoVenta'].sum() / df_filtrado['IDFactura'].nunique():,.2f}",
)
# Unidades Vendidas: cantidad total de productos vendidos
col6.metric(label="Unidades Vendidas", value=f"{df_filtrado['Cantidad'].sum():,.0f}")

# Unidades por Ticket: cuántos productos compra en promedio cada cliente
col7.metric(
    label="Unidades por Ticket",
    value=f"{df_filtrado['Cantidad'].sum() / df_filtrado['IDFactura'].nunique():,.2f}",
)

# -------------------------------------------------------------------
# ANÁLISIS VISUAL - GRÁFICOS
# -------------------------------------------------------------------
# Aquí creamos gráficos interactivos para entender mejor los datos.
# Usamos Plotly Express, que hace gráficos bonitos con poco código.
#
# El proceso general es siempre el mismo:
#   1. Preparamos los datos (agrupamos, sumamos, ordenamos).
#   2. Creamos el gráfico con una función de Plotly Express.
#   3. Mostramos el gráfico en la página con st.plotly_chart().

st.subheader("Análisis Visual")

# Dividimos el espacio en 2 columnas para poner un gráfico en cada una
col8, col9 = st.columns(2)

with col8:
    # ---- Gráfico de pastel: Ventas por ciudad ----
    # st.markdown() nos permite escribir texto con formato.
    # El **texto** se ve en negrita gracias a Markdown, un lenguaje
    # sencillo para dar estilo al texto (como WhatsApp o Discord).
    st.markdown("**Ventas por ciudad**")

    # PASO 1: Agrupar los datos por ciudad y sumar los montos de venta.
    # groupby() agrupa filas que comparten un mismo valor (ej: misma ciudad).
    # reset_index() convierte el resultado de vuelta a un DataFrame normal.
    # sort_values() ordena de mayor a menor (ascending=False).
    ventas_por_ciudad = (
        df_filtrado.groupby("Ciudad")["MontoVenta"]
        .sum()
        .reset_index()
        .sort_values(by="MontoVenta", ascending=False)
    )

    # PASO 2: Creamos un gráfico de pastel (pie chart).
    # - values: la columna con los números (el tamaño de cada porción).
    # - names: la columna con las etiquetas (los nombres de cada porción).
    # - hole: hace un agujero en el centro (como una dona).
    # - color_discrete_map: elegimos colores específicos para cada ciudad.
    pie_chart_ciudad = px.pie(
        ventas_por_ciudad,
        values="MontoVenta",
        names="Ciudad",
        color="Ciudad",
        color_discrete_map={
            "Mandalay": "#8542cd",
            "Naypytaw": "#de8d1b",
            "Yangon": "#2771cc",
        },
        hole=0.5,
    )

    # PASO 3: Mostramos el gráfico en la página
    st.plotly_chart(pie_chart_ciudad, use_container_width=True)


with col9:
    # ---- Gráfico de pastel: Ventas por método de pago ----
    st.markdown("**Ventas por método de pago**")

    ventas_por_metodo_pago = (
        df_filtrado.groupby("MetodoPago")["MontoVenta"]
        .sum()
        .reset_index()
        .sort_values(by="MontoVenta", ascending=True)
    )
    fig_pie_metodo_pago = px.pie(
        ventas_por_metodo_pago,
        values="MontoVenta",
        names="MetodoPago",
        hole=0.5,
    )
    st.plotly_chart(fig_pie_metodo_pago, use_container_width=True)

# ---- Gráfico de barras: Ventas por clasificación de producto ----
st.markdown("**Ventas por clasificación de producto**")

ventas_por_clasificacion = (
    df_filtrado.groupby("ClasificacionProducto")["MontoVenta"]
    .sum()
    .reset_index()
    .sort_values(by="MontoVenta", ascending=True)
)
fig_bar_clasificacion = px.bar(
    ventas_por_clasificacion,
    x="MontoVenta",
    y="ClasificacionProducto",
    # color: las barras se colorean según su valor (más venta = color más intenso)
    color="MontoVenta",
    # color_continuous_scale: elegimos una paleta de colores (Plasma es una de ellas)
    color_continuous_scale=px.colors.sequential.Plasma,
    # orientation="h": barras horizontales. Si lo omitimos, serían verticales.
    orientation="h",
)
st.plotly_chart(fig_bar_clasificacion, use_container_width=True)

# ---- Gráfico de líneas: Evolución de ventas en el tiempo ----
st.markdown("**Evolución de ventas por fecha**")

# El usuario puede elegir si quiere ver los datos por día, semana, mes o año
unidad_tiempo = st.selectbox(
    "Seleccione la unidad de tiempo para la evolución de ventas",
    options=["Día", "Semana", "Mes", "Año"],
    key="unidad_tiempo",
)

# Agrupamos las ventas por fecha usando pd.Grouper.
# Grouper es una herramienta de Pandas que agrupa fechas en intervalos
# (días, semanas, meses, años). La frecuencia (freq) se elige según
# lo que el usuario seleccionó:
#   "Día"    -> "D"   (day)
#   "Semana" -> "W"   (week)
#   "Mes"    -> "ME"  (month end)
#   "Año"    -> "YE"  (year end)
ventas_por_fecha = (
    df_filtrado.groupby(
        pd.Grouper(
            key="Fecha",
            freq={
                "Día": "D",
                "Semana": "W",
                "Mes": "ME",
                "Año": "YE",
            }[unidad_tiempo],
        )
    )["MontoVenta"]
    .sum()
    .reset_index()
    .sort_values(by="Fecha", ascending=True)
)
fig_line_fecha = px.line(
    ventas_por_fecha,
    x="Fecha",
    y="MontoVenta",
    # markers=True: muestra un puntito en cada fecha con datos
    markers=True,
    # color_discrete_sequence: elegimos colores llamativos para la línea
    color_discrete_sequence=px.colors.qualitative.Vivid,
)
st.plotly_chart(fig_line_fecha, use_container_width=True)

# -------------------------------------------------------------------
# TABLA DE DATOS FILTRADOS
# -------------------------------------------------------------------
# Finalmente, mostramos los datos ya filtrados en una tabla interactiva.
# El usuario puede ver fila por fila la información de cada venta,
# ordenar las columnas y buscar valores específicos.
st.divider()
st.dataframe(df_filtrado)
