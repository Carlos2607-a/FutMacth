import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
import unicodedata
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import streamlit as st

def importar_datos(posicion):
    filename = f"/workspaces/Proyecto_Knn_Players/Data Posición/df_{posicion}_medias.csv.csv"
    return pd.read_csv(filename)

print("Bienvenido a la página web de Fútbol Estadísticas!")

opciones = ["delanteros", "medio", "defensas", "porteros"]
for i, opcion in enumerate(opciones, 1):
    print(f"{i}. {opcion}")

numero = int(input("¿Qué posición deseas consultar? (ingresa el número correspondiente): "))
posicion = opciones[numero - 1]

dataframe = importar_datos(posicion)


