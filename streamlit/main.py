import streamlit as st
import pandas as pd 

st.title("Primeira aplicação data :alien:")

st.write("""
    Hello, **world** :sunglasses:!
""")

#df = pd.DataFrame({
#    'Pessoa' : ['Italo', 'dan', 'Voyager'],
#    'Forma de contato':['email', 'Telefone', 'Outros'] 
#})
#st.write(df)

df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")
df.drop(columns='Unnamed: 0', inplace=True)
st.write(df)

escolha = st.selectbox("Escolha uma das linguagens", df["Linguagem"].unique())


click = st.button('Enviar')

if click:
    df_filter = df.loc[df['Linguagem'] == escolha]
    st.dataframe(df_filter)

upload = st.file_uploader("Faça o upload de um arquivo")
if upload:
    if 'jpeg' in upload.type:
        st.image(upload)
    if 'csv' in upload.type:
        file = pd.read_csv(upload, sep=",")
        st.dataframe(file)

st.bar_chart(df, x = 'Linguagem', y='Desenvolvedores', color='Linguagem')
st.bar_chart(df, x='Popularidade', y='Desenvolvedores')
st.scatter_chart(df, x='Linguagem', y='Desenvolvedores', color='Linguagem')