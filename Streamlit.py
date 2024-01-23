import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
import unicodedata
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import streamlit as st
from Funciones import buscar_jugadores_similares_defensas

# Configura la página para usar el modo ancho
st.set_page_config(layout="wide")

# Usamos el decorador de caché para almacenar los resultados de esta función
@st.cache
def importar_datos(posicion):
    filename = f"Data Posición/df_{posicion}_medias.csv"
    df = pd.read_csv(filename)
    return df

st.write("Bienvenido a la página web de Fútbol Estadísticas!")

opciones = ["delanteros", "medio", "defensas", "porteros"]
opcion = st.selectbox("¿Qué posición deseas consultar?", opciones)

Data = importar_datos(opcion)

nombre_jugador = st.text_input("Introduce el nombre del jugador que deseas buscar")

if opcion == "defensas":
    # Asume que buscar_jugadores_similares_defensas() devuelve una figura de Plotly
    fig = buscar_jugadores_similares_defensas(nombre_jugador)
    
    # Crea tres columnas con tamaños personalizados
col1, col2, col3 = st.columns([1, 2, 1])

# Coloca tu gráfico en la columna del medio
with col2:
    st.plotly_chart(fig)







