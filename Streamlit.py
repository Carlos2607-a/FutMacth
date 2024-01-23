import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
import unicodedata
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import streamlit as st


# Usamos el decorador de caché para almacenar los resultados de esta función
@st.cache
def importar_datos(posicion):
    filename = f"/workspaces/Proyecto_Knn_Players/Data Posición/df_{posicion}_medias.csv"
    df = pd.read_csv(filename)
    return df


st.write("Bienvenido a la página web de Fútbol Estadísticas!")

opciones = ["delanteros", "medio", "defensas", "porteros"]
opcion = st.selectbox("¿Qué posición deseas consultar?", opciones)

dataframe = importar_datos(opcion)
# Aquí puedes agregar código para mostrar el DataFrame en tu aplicación Streamlit



