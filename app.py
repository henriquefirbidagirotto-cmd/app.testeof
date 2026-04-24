import streamlit as st
import pandas as pd
import numpy as np

dados = {
    'dia': [1,2,3,4,5],
    'vendas': [500,450,400,350,300]
}

df = pd.DataFrame(dados)
if st.button('Gerar Grafico'):
    st.line_chart(df.set_index('dia'))


st.title('Ler o CSV')

arquivo = st.file_uploader('Enviar CSV', type=['csv'])

if arquivo:
    df = pd.read_csv('dado.csv')
    st.write('dados')
    st.dataframe(df)
    if st.button('Gerar um Grafico'):
        st.line_chart(df['venda'])   





st.title('imagem', 'url')

st.image('img.jpg', caption=('image'))

url = st.text_input('Insira a url')

if url:
    st.image(url, caption=('image'))