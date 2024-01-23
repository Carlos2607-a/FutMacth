import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go
import unicodedata
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def buscar_jugadores_similares_defensas(nombre):

    Data = pd.read_csv("Data Posición/df_defensas_medias.csv")
    pd.set_option('display.max_columns', None)

    Data.fillna((0),inplace=True)

    Columna_habilidades = Data.columns.drop(["Name", "League"])
    features = Data[Columna_habilidades]
    # Crea un objeto MinMaxScaler
    scaler = MinMaxScaler()
    # Ajusta el escalador a tus datos y luego transforma tus datos
    features_scaled = scaler.fit_transform(features)
    # Inicializa el modelo NearestNeighbors
    model = NearestNeighbors(n_neighbors=5)  # Buscamos 4 vecinos porque uno de ellos será el jugador mismo
    # Ajusta el modelo a tus datos
    model.fit(features_scaled)
    caracteristicas_grafico = ['Errors lead to goal','Interceptions','Penalty committed','Clearances','Tackles','Dribbled past','Total passes']

    columnas_a_dividir = ['Total passes','Accurate passes %', 'Accurate final third passes',
       'Accurate long balls %','Aerial duels won %', 'Total duels won %']

    # Divide todos los datos de las columnas por 10
    Data[columnas_a_dividir] = Data[columnas_a_dividir] / 10
    jugador = Data[Data['Name'] == nombre]

    Clearances_media = Data["Clearances"].mean()
    Clearances_min = Data["Clearances"].min()
    Clearances_max = Data["Clearances"].max()
    
    Aerial_duels_won_media = Data["Aerial duels won %"].mean()
    Aerial_duels_won_min = Data["Aerial duels won %"].min()
    Aerial_duels_won__max = Data["Aerial duels won %"].max()
    
    Goals_conceded_inside_media = Data["Goals conceded inside the box"].mean()
    Goals_conceded_inside_min = Data["Goals conceded inside the box"].min()
    Goals_conceded_inside_max = Data["Goals conceded inside the box"].max()
    
    Tackles_media = Data["Tackles"].mean()
    Tackles_min = Data["Tackles"].min()
    Tackles_max = Data["Tackles"].max()
    
    Accurate_final_third_passesmedia = Data["Accurate final third passes"].mean()
    Accurate_final_third_passesmin = Data["Accurate final third passes"].min()
    Accurate_final_third_passesmax = Data["Accurate final third passes"].max()
    
    creadas_media = Data["Big chances created"].mean()
    creadas_min = Data["Big chances created"].min()
    creadas_max = Data["Big chances created"].max()
    
    if len(jugador) == 0:
        return 'Jugador no encontrado'
    else:
        jugador_scaled = scaler.transform(jugador[features.columns])  # Normalización para el modelo
        distancias, indices = model.kneighbors(jugador_scaled)
        jugadores_similares = Data.iloc[indices[0][0:]] 
        colores = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
        
        # Agregar 'Media' a la lista de jugadores similares antes de mostrar el DataFrame
        jugadores_similares = pd.concat([jugadores_similares, Data[Data['Name'] == 'Media']])
        st.dataframe(jugadores_similares)

        # Escala todas las características de los jugadores similares
        fig = go.Figure()
        for i, row in enumerate(jugadores_similares[caracteristicas_grafico].values):  # Usamos los valores originales aquí
            fig.add_trace(go.Scatterpolar(
                r=row,
                theta=caracteristicas_grafico,
                fill='toself',
                name=jugadores_similares.iloc[i]['Name']
            ))
        fig.update_layout(
            autosize=False,
            width=1000,
            height=1000,
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[-2, 7]  # Ajusta este rango según tus datos
                )),
            showlegend=True
        )
        st.plotly_chart(fig)
        
       # Configura una cuadrícula de subplots con 3 filas y 2 columnas
        fig, axs = plt.subplots(3, 2, figsize=(20, 15))  # Ajusta el tamaño según sea necesario
        # Gráfico de dispersión para Clearances
        for i, name in enumerate(jugadores_similares['Name']):
            axs[0, 0].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Clearances'], color=colores[i % len(colores)], marker='o')
        for line in [Clearances_max, Clearances_media, Clearances_min]:
            axs[0, 0].axhline(y=line, color='r', linestyle='--')
        axs[0, 0].set_title('Comparativa de Clearances de los jugadores similares')
        axs[0, 0].set_xticks(range(len(jugadores_similares)))
        axs[0, 0].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[0, 0].set_xlabel('Jugadores')
        axs[0, 0].set_ylabel('Clearances')
        # Gráfico de dispersión para Aerial duels won %
        for i, name in enumerate(jugadores_similares['Name']):
            axs[0, 1].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Aerial duels won %'], color=colores[i % len(colores)], marker='o')
        for line in [Aerial_duels_won__max, Aerial_duels_won_media, Aerial_duels_won_min]:
            axs[0, 1].axhline(y=line, color='r', linestyle='--')
        axs[0, 1].set_title('Media de Aerial duels won % de los jugadores similares')
        axs[0, 1].set_xticks(range(len(jugadores_similares)))
        axs[0, 1].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[0, 1].set_xlabel('Jugadores')
        axs[0, 1].set_ylabel('Aerial duels won %')
        # Gráfico de dispersión para Goals conceded inside the box
        for i, name in enumerate(jugadores_similares['Name']):
            axs[1, 0].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Goals conceded inside the box'], color=colores[i % len(colores)], marker='o')
        for line in [Goals_conceded_inside_max, Goals_conceded_inside_media, Goals_conceded_inside_min]:
            axs[1, 0].axhline(y=line, color='r', linestyle='--')
        axs[1, 0].set_title('Media de Goals conceded inside the box de los jugadores similares')
        axs[1, 0].set_xticks(range(len(jugadores_similares)))
        axs[1, 0].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[1, 0].set_xlabel('Jugadores')
        axs[1, 0].set_ylabel('Goals conceded inside the box')
        # Gráfico de dispersión para Tackles
        for i, name in enumerate(jugadores_similares['Name']):
            axs[1, 1].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Tackles'], color=colores[i % len(colores)], marker='o')
        for line in [Tackles_max, Tackles_media, Tackles_min]:
            axs[1, 1].axhline(y=line, color='r', linestyle='--')
        axs[1, 1].set_title('Media de Tackles de los jugadores similares')
        axs[1, 1].set_xticks(range(len(jugadores_similares)))
        axs[1, 1].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[1, 1].set_xlabel('Jugadores')
        axs[1, 1].set_ylabel('Tackles')
        # Gráfico de dispersión para Accurate final third passes
        for i, name in enumerate(jugadores_similares['Name']):
            axs[2, 0].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Accurate final third passes'], color=colores[i % len(colores)], marker='o')
        for line in [Accurate_final_third_passesmax, Accurate_final_third_passesmedia, Accurate_final_third_passesmin]:
            axs[2, 0].axhline(y=line, color='r', linestyle='--')
        axs[2, 0].set_title('Media de Accurate final third passes de los jugadores similares')
        axs[2, 0].set_xticks(range(len(jugadores_similares)))
        axs[2, 0].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[2, 0].set_xlabel('Jugadores')
        axs[2, 0].set_ylabel('Accurate final third passes')
        # Gráfico de dispersión para Big chances created
        for i, name in enumerate(jugadores_similares['Name']):
            axs[2, 1].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Big chances created'], color=colores[i % len(colores)], marker='o')
        for line in [creadas_max, creadas_media, creadas_min]:
            axs[2, 1].axhline(y=line, color='r', linestyle='--')
        axs[2, 1].set_title('Media de Total duels won % de los jugadores similares')
        axs[2, 1].set_xticks(range(len(jugadores_similares)))
        axs[2, 1].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[2, 1].set_xlabel('Jugadores')
        axs[2, 1].set_ylabel('Big chances created')

        plt.tight_layout()
        # Ajusta el layout para que no haya superposición de elementos
          
   
        
        st.pyplot(fig)
        return


def buscar_jugadores_similares_delanteros(nombre):

    Data = pd.read_csv("Data Posición/df_delanteros_medias.csv")
    pd.set_option('display.max_columns', None)

    Data.fillna((0),inplace=True)

    Columna_habilidades = Data.columns.drop(["Name", "League"])
    features = Data[Columna_habilidades]
    # Crea un objeto MinMaxScaler
    scaler = MinMaxScaler()
    # Ajusta el escalador a tus datos y luego transforma tus datos
    features_scaled = scaler.fit_transform(features)
    # Inicializa el modelo NearestNeighbors
    model = NearestNeighbors(n_neighbors=5)  # Buscamos 4 vecinos porque uno de ellos será el jugador mismo
    # Ajusta el modelo a tus datos
    model.fit(features_scaled)
    caracteristicas_grafico = ['Big chances missed','Big chances created','Headed goals','Total shots','Goals','Was fouled','Assists','Set piece conversion %','Accurate passes %','Successful dribbles %','Total duels won %','Aerial duels won %']
    
    columnas_a_dividir = ['Successful dribbles %', 'Accurate passes %', 'Aerial duels won %','Total duels won %']

    # Divide todos los datos de las columnas por 10
    Data[columnas_a_dividir] = Data[columnas_a_dividir] / 10

    jugador = Data[Data['Name'] == nombre]

    Goals_media = Data["Goals"].mean()
    Goals_min = Data["Goals"].min()
    Goals_max = Data["Goals"].max()

    Headed_goals_media = Data["Headed goals"].mean()
    Headed_goals_min = Data["Headed goals"].min()
    Headed_goals_max = Data["Headed goals"].max()

    Missed_media = Data["Big chances missed"].mean()
    Missed_min = Data["Big chances missed"].min()
    Missed_max = Data["Big chances missed"].max()

    Aerial_duels_won_media = Data["Aerial duels won %"].mean()
    Aerial_duels_won_min = Data["Aerial duels won %"].min()
    Aerial_duels_won__max = Data["Aerial duels won %"].max()

    Assists_media = Data["Assists"].mean()
    Assists_min = Data["Assists"].min()
    Assists_max = Data["Assists"].max()

    Big_chances_created_media = Data["Big chances created"].mean()
    Big_chances_created_min = Data["Big chances created"].min()
    Big_chances_created_max = Data["Big chances created"].max()

    
    if len(jugador) == 0:
        return 'Jugador no encontrado'
    else:
        jugador_scaled = scaler.transform(jugador[features.columns])  # Normalización para el modelo
        distancias, indices = model.kneighbors(jugador_scaled)
        jugadores_similares = Data.iloc[indices[0][0:]]  
        colores = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
        
        # Agregar 'Media' a la lista de jugadores similares antes de mostrar el DataFrame
        jugadores_similares = pd.concat([jugadores_similares, Data[Data['Name'] == 'Media']])
        st.dataframe(jugadores_similares)

        # Escala todas las características de los jugadores similares
        fig = go.Figure()
        for i, row in enumerate(jugadores_similares[caracteristicas_grafico].values):  # Usamos los valores originales aquí
            fig.add_trace(go.Scatterpolar(
                r=row,
                theta=caracteristicas_grafico,
                fill='toself',
                name=jugadores_similares.iloc[i]['Name']
            ))
        fig.update_layout(
            autosize=False,
            width=1000,
            height=1000,
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[-2, 7]  # Ajusta este rango según tus datos
                )),
            showlegend=True
        )
        st.plotly_chart(fig)
        
       # Configura una cuadrícula de subplots con 3 filas y 2 columnas
        fig, axs = plt.subplots(3, 2, figsize=(20, 12))  # Ajusta el tamaño según sea necesario
        # Gráfico de dispersión para Big chances missed
        for i, name in enumerate(jugadores_similares['Name']):
            axs[0, 0].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Big chances missed'], color=colores[i % len(colores)], marker='o')
        for line in [Missed_max, Missed_media, Missed_min]:
            axs[0, 0].axhline(y=line, color='r', linestyle='--')
        axs[0, 0].set_title('Comparativa de Big chances missed de los jugadores similares')
        axs[0, 0].set_xticks(range(len(jugadores_similares)))
        axs[0, 0].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[0, 0].set_xlabel('Jugadores')
        axs[0, 0].set_ylabel('Big chances missed')
        # Gráfico de dispersión para la media Goals
        for i, name in enumerate(jugadores_similares['Name']):
            axs[0, 1].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Goals'], color=colores[i % len(colores)], marker='o')
        for line in [Goals_max, Goals_media, Goals_min]:
            axs[0, 1].axhline(y=line, color='r', linestyle='--')
        axs[0, 1].set_title('Comparativa de Goals de los jugadores similares')
        axs[0, 1].set_xticks(range(len(jugadores_similares)))
        axs[0, 1].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[0, 1].set_xlabel('Jugadores')
        axs[0, 1].set_ylabel('Goals')
        # Gráfico de dispersión para la media Headed goals
        for i, name in enumerate(jugadores_similares['Name']):
            axs[1, 0].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Headed goals'], color=colores[i % len(colores)], marker='o')
        for line in [Headed_goals_max, Headed_goals_media, Headed_goals_min]:
            axs[1, 0].axhline(y=line, color='r', linestyle='--')
        axs[1, 0].set_title('Comparativa de Headed goals de los jugadores similares')
        axs[1, 0].set_xticks(range(len(jugadores_similares)))
        axs[1, 0].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[1, 0].set_xlabel('Jugadores')
        axs[1, 0].set_ylabel('Headed goals')
        # Gráfico de dispersión para Aerial duels won %
        for i, name in enumerate(jugadores_similares['Name']):
            axs[1, 1].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Aerial duels won %'], color=colores[i % len(colores)], marker='o')
        for line in [Aerial_duels_won__max, Aerial_duels_won_media, Aerial_duels_won_min]:
            axs[1, 1].axhline(y=line, color='r', linestyle='--')
        axs[1, 1].set_title('Comparativa de Aerial duels won  de los jugadores similares')
        axs[1, 1].set_xticks(range(len(jugadores_similares)))
        axs[1, 1].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[1, 1].set_xlabel('Jugadores')
        axs[1, 1].set_ylabel('Aerial duels won %')
        # Gráfico de dispersión para la media Assists
        for i, name in enumerate(jugadores_similares['Name']):
            axs[2, 0].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Assists'], color=colores[i % len(colores)], marker='o')
        for line in [Assists_max, Assists_media, Assists_min]:
            axs[2, 0].axhline(y=line, color='r', linestyle='--')
        axs[2, 0].set_title('Comparativa de Assists de los jugadores similares')
        axs[2, 0].set_xticks(range(len(jugadores_similares)))
        axs[2, 0].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[2, 0].set_xlabel('Jugadores')
        axs[2, 0].set_ylabel('Assists')
        # Gráfico de dispersión para la media Big chances created
        for i, name in enumerate(jugadores_similares['Name']):
            axs[2, 1].scatter(i, jugadores_similares.loc[jugadores_similares['Name'] == name, 'Big chances created'], color=colores[i % len(colores)], marker='o')
        for line in [Big_chances_created_max, Big_chances_created_media, Big_chances_created_min]:
            axs[2, 1].axhline(y=line, color='r', linestyle='--')
        axs[2, 1].set_title('Comparativa de Big chances created de los jugadores similares')
        axs[2, 1].set_xticks(range(len(jugadores_similares)))
        axs[2, 1].set_xticklabels(jugadores_similares['Name'], rotation=45)
        axs[2, 1].set_xlabel('Jugadores')
        axs[2, 1].set_ylabel('Big chances created')
        # Ajusta el layout para que no haya superposición de elementos
        plt.tight_layout()
        st.pyplot(fig)
        return
    

