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

# Configura el título y la descripción de la aplicación
st.title("Buscador de Jugadores Similares")
st.write("Introduce el nombre del jugador que deseas buscar:")

# Solicita al usuario que introduzca el nombre del jugador
nombre_jugador = st.text_input("introduzca el nombre del jugador")

# Convierte la entrada del usuario a minúsculas
nombre_jugador = nombre_jugador.lower()

# Llama a tu función con el nombre del jugador
resultado = buscar_jugadores_similares_defensas(nombre_jugador)

# Muestra el resultado
st.write(resultado)
