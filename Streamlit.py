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
from Funciones import buscar_jugadores_similares_delanteros


# Configura la página para usar el modo ancho
st.set_page_config(layout="wide")

# Usamos el decorador de caché para almacenar los resultados de esta función
st.write("Bienvenido a la página web de Fútbol Estadísticas!")

opciones = ["delanteros", "medio", "defensas", "porteros"]
opcion = st.selectbox("¿Qué posición deseas consultar?", opciones)

nombre_jugador = st.text_input("Introduce el nombre del jugador que deseas buscar")

if opcion == "defensas":
    buscar_jugadores_similares_defensas(nombre_jugador)
elif opcion == "delanteros":
    buscar_jugadores_similares_delanteros(nombre_jugador)





