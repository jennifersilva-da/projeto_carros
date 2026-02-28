import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('notebooks/vehicles_us.csv')

st.header("Análise de Dados de Carros")

hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')
if scatter_button:
    st.write('Criando gráfico de dispersão: Quilometragem vs Preço')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)