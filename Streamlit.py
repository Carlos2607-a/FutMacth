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
from Funciones import buscar_jugadores_similares_medios
from Funciones import buscar_jugadores_similares_porteros


# Configura la página para usar el modo ancho
st.set_page_config(layout="wide")


st.write("Bienvenido ala aplicación de FutMatch!")

opciones = ["Delanteros", "Mediocampista", "Defensas", "Porteros"]
opcion = st.selectbox("¿Qué posición deseas consultar?", opciones)

nombre_jugador = st.text_input("Introduce el nombre del jugador que deseas buscar")

if opcion == "Defensas":
    buscar_jugadores_similares_defensas(nombre_jugador)
elif opcion == "Delanteros":
    buscar_jugadores_similares_delanteros(nombre_jugador)
elif opcion == "Mediocampista":
    buscar_jugadores_similares_medios(nombre_jugador)
elif opcion == "Porteros":
    buscar_jugadores_similares_porteros(nombre_jugador)
else:
    pass





