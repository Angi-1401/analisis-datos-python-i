import pandas as pd
import streamlit as st

df = pd.read_csv("supermercado.csv")

st.title("Ventas")


def limpiar_filtros():
    st.session_state["fecha_inicio"] = pd.to_datetime(df["Fecha"].min())
    st.session_state["fecha_fin"] = pd.to_datetime(df["Fecha"].max())
    st.session_state["clasificaciones"] = None
    st.session_state["id_venta"] = ""


# --------------------
# Sidebar - Filtros
# --------------------

st.sidebar.title("Filtros")

st.sidebar.subheader("Filtrar por fecha")
fecha_inicio = st.sidebar.date_input(
    "Fecha de inicio", value=pd.to_datetime(df["Fecha"].min()), key="fecha_inicio"
)
fecha_fin = st.sidebar.date_input(
    "Fecha de fin", value=pd.to_datetime(df["Fecha"].max()), key="fecha_fin"
)

st.sidebar.subheader("Filtrar por clasificación de producto")
clasificaciones = df["ClasificacionProducto"].unique()
clasificacion_seleccionada = st.sidebar.selectbox(
    "Seleccione las clasificaciones de producto",
    options=clasificaciones,
    key="clasificaciones",
)

st.sidebar.divider()
st.sidebar.button("Limpiar filtros", on_click=limpiar_filtros, key="limpiar_filtros")

"""
Utiliza st.selectbox para crear selecciones simples.
Utiliza st.multiselect para permitir la selección de múltiples opciones.

Nota: st.multiselect requiere un parámetro adicional llamado 'default' para establecer las opciones seleccionadas por defecto.
"""

# --------------------
# Métricas clave
# --------------------

# --------------------
# Búsqueda por ID de venta
# --------------------

st.subheader("Búsqueda")
id_venta = st.text_input("Ingrese el ID de la venta que desea buscar:", key="id_venta")

df_filtrado = df[df["IDFactura"] == id_venta] if id_venta else df

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

df_filtrado = (
    df_filtrado[df_filtrado["ClasificacionProducto"] == clasificacion_seleccionada]
    if clasificacion_seleccionada
    else df
)


st.dataframe(df_filtrado)

# Ejercicios
# Crear un widget que permita filtrar por selección simple
# la Rama de una venta.
# Crear un widget que permita filtrar por selección múltiple
# la Ciudad de una venta.