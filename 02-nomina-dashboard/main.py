import streamlit as st
import pandas as pd

df = pd.read_csv("nomina.csv")

st.title("Dashboard preliminar de empleados")

st.write("Este es un dashboard preliminar para visualizar información de empleados.")

st.text("A continuación, se muestra un ejemplo de cómo visualizar datos de empleados.")

st.header("Empleados")

st.subheader("Métricas clave")

st.metric("Número total de empleados", len(df))
st.metric("Salario promedio", df["SalarioNeto"].mean())
st.metric("Salario máximo", df["SalarioNeto"].max())
st.metric("Salario mínimo", df["SalarioNeto"].min())

st.subheader("Tabla de empleados")
st.dataframe(df)
