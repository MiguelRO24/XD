import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Nombre de la pestaña
st.set_page_config(layout= 'centered', page_title= 'mi primer pericaso', page_icon= ':smile:')

# Titulo de la pagina
t1, t2 = st.columns([0.3, 0.7])
t1.image('Diomedes.jpg', width = 200)
t2.title('mi primer tablero')
t2.markdown('**tel:** 3122132311 **| email:** miguel.rodriguezo@udea.edu.co')

# Secciones
steps = st.tabs(['Pestaña 1', 'Pestaña 2', 'Pestaña $\sqrt{9}$'])
with steps[0]:
    st.write('Hola mundo')
    st.image('Diomedes.jpg', width = 50)
    data = {'Nombre': ['Adan', 'Eva'], 'Fecha de nacimiento':[0, 0]}
    df = pd.DataFrame(data)
    st.table(df)
    st.dataframe(df)

with steps[1]:
    if st.button('Podemos usar botones', type = 'primary'):
        st.write('usted presionó el botón')

with steps[2]:
    st.selectbox('Escoja una opción', ['Opción 1', 'Opción 2', 'Opción3'])

with steps[0]:
    camp_df = pd.read_csv('Campanhas.csv', encoding='latin-1', sep = ';')
    camp = st.selectbox('Escoge un ID de campaña', camp_df['ID_Campana'], help='Muestra las campañas existentes')

    met_df = pd.read_csv('Metricas.csv', encoding='latin-1', sep = ';')

    m1, m2, m3 = st.columns([1, 1, 1])

    id1 = met_df[(met_df['ID_Campana']==camp)]
    id2 = met_df[met_df['ID_Campana']==camp] 
    m1.write('Metricas filtradas')
    m1.metric(label = 'Metrica 1',value = sum(id1['Conversiones']),
    delta=str(sum(id1['Rebotes']))+ 'Numero de Rebotes', 
    delta_color='inverse')
    m2.metric(label = 'Metrica 2',value = np.mean(id1['Conversiones']),
    delta=str(np.mean(id1['Rebotes']))+ 'Promedios', 
    delta_color='inverse')

with steps[1]:
    varx= st.selectbox('Escoge ID Metrica', met_df['ID_Metrica'])
    vary= st.selectbox('Escoger número de conversiónes', met_df['Conversiones'])
    fig, ax = plt.subplots()
    ax = sns.scatterplot(data=met_df, x = varx, y = vary, hue = 'ID_Campana')
    st.pyplot(fig) 


with steps[1]:
    df = pd.read_csv("https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso1/master/s03/dataVentas2009.csv")
    df.Fecha = pd.to_datetime(df.Fecha, format = '%d/%m/%Y')
    df.set_index('Fecha', inplace = True)
    varx= st.selectbox('Escoge la variable x', df.columns)
    #vary= st.selectbox('Escoger la variable y', met_df['Clic'])
    fig, ax = plt.subplots()
    ax = sns.histplot(data=df, x=varx)
    st.pyplot(fig) 
