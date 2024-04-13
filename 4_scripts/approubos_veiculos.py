# importando as bibliotecas

import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import sqlite3


# Nome da aplicação
st.markdown("<h2 style='font-family: Cascadia Code;'>Roubo de Veiculos", unsafe_allow_html=True)
st.write('São Paulo-SP')


#criando uma função que chama a base de dados

def get_data():
    path = '../1_bases_tratadas/roubo_veiculos_tratado.csv'
    return pd.read_csv(path, sep=';')

df = get_data()

variaveis = df.columns
st.sidebar.header('Escolha uma variável')
escolha_variavel = st.sidebar.selectbox("Escolha a variavel", variaveis)
#data ocorrencia
if escolha_variavel == 'Data_Ocorrencia':
    st.write('Grafico Univariado')
    st.write('**Foi observado que em 08/03/2022 ocorreu a maior quantidade de roubos de veículos.**')
    st.write('''**E em 15/01/2019 ocorreu a menor quantidade de roubos de veículos,
                no periodo de 3 anos conseguimos visualizar o maior pico de roubos em nossa base.**''')
    fig1 = px.histogram(df,y="Data_Ocorrencia")
    st.plotly_chart(fig1)


elif escolha_variavel == 'Periodo_Ocorrencia':
    st.write('Grafico Univariado')
    st.write('**As maiores frequências de crimes ocorrem nos periodos noturno, matutino e pela madrugada.**')
    fig1 = px.histogram(df,"Periodo_Ocorrencia")
    st.plotly_chart(fig1)


elif escolha_variavel == 'Cidade':
    st.write('Grafico Univariado')
    st.write('''**Observamos que a cidade em que houve a maior quantidade de roubos, foi São Paulo-SP,
                seguido de Guarulhos e S.Bernado do Campo.**''')
    fig1 = px.histogram(df,y="Cidade")
    st.plotly_chart(fig1)


elif escolha_variavel == 'Flagrante':
    st.write('Grafico Univariado')
    st.write('**Podemos observar que 84.5% dos roubos de veiculo, não houve flagrante.**')
    labels = ['Sim', 'Não']
    values = [3351,18329]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(legend=dict(title='Flagrantes', orientation='h', yanchor='bottom', y=-0.2))
    st.plotly_chart(fig)


elif escolha_variavel == 'Descr_Automovel':
    st.write('Grafico Univariado')
    st.write('**Os veiculos que obtiveram mais ocorrência de roubo, foram respectivamente, Automovel, Motocicleta e Caminhonete.**')
    fig1 = px.histogram(df,y="Descr_Automovel")
    st.plotly_chart(fig1)
    

