import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('notebooks/vehicles_us.csv')

st.header("Análise de Dados de Carros")

hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)