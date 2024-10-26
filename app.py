import streamlit as st
import pandas as pd
import plotly_express as px

st.title('Visualización de Anuncios de Venta de Coches')
st.write("Explora el conjunto de datos de vehículos de segunda mano.")

try:
    car_data = pd.read_csv('/Users/tomaster/vehicles_env/vehicles_us - vehicles_us.csv') # leer los datos
    st.success("Datos cargados correctamente.")
except FileNotFoundError:
    st.error("Archivo no encontrado. Por favor, verifica la ubicación y el nombre del archivo.")

# Seleccionar columna para el histograma

st.sidebar.header("Configuración del Histograma")
hist_x_column = st.sidebar.selectbox("Selecciona la columna para el eje X", options=car_data.columns)
hist_button = st.button('Construir histograma')

if hist_button: 
    st.write(f'Creación de un histograma para la columna seleccionada: **{hist_x_column}**')
    fig = px.histogram(car_data, x=hist_x_column, color_discrete_sequence=['#636EFA'])
    st.plotly_chart(fig, use_container_width=True)




# Seleccionar columna para el gráfico de dispersión
st.sidebar.header("Configuración del gráfico de dispersión")

scatter_x_column = st.sidebar.selectbox("Selecciona la columna para el eje X del gráfico de dispersión", options=car_data.columns, key="scatter_x")
scatter_y_column = st.sidebar.selectbox("Selecciona la columna para el eje Y del gráfico de dispersión", options=car_data.columns, key="scatter_y")

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write(f'Creación de un gráfico de dispersión para las columnas seleccionadas: **{scatter_x_column}** y **{scatter_y_column}**')
    scatter_fig = px.scatter(car_data, x=scatter_x_column, y=scatter_y_column, color_discrete_sequence=['#EF553B'])


# Configuración del Boxplot
st.sidebar.header("Configuración del Boxplot")
box_y_column = st.sidebar.selectbox("Selecciona la columna para el eje Y del boxplot", options=car_data.columns, key="box_y")

box_button = st.button('Construir boxplot')

if box_button:
    st.write(f'Creación de un boxplot para la columna seleccionada: **{box_y_column}**')
    box_fig = px.box(car_data, y=box_y_column, color_discrete_sequence=['#00CC96'])
    st.plotly_chart(box_fig, use_container_width=True)