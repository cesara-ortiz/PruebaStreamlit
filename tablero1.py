import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='centered',page_title= 'Talento Tech',page_icon=':angry:')

t1, t2 = st.columns([0.3, 0.7])
t1.image('images.jpg', width=200)
t2.title('Mi primer tablero')
t2.markdown('tel:123 | cesara.ortiz@udea.edu.co')

# Secciones 
steps = st.tabs(['Pestaña', 'Pestaña 2', 'Pestaña $\sqrt{9}$', 'Otra Pestaña'])

# Agregar cosas a la primera pestaña
with steps[0]:
    st.write('Hola Mundo!')
    st.image('images.jpg', width=70)
    data = {'nombre': ['Adan', 'Eva'], 
        'Fecha de nacimiento': [0,0]}
    df= pd.DataFrame(data)
    st.table(df)
    st.dataframe(df) # es mejor montarlo directamente como dataframe que como tabla

# Agregar cosas a la segunda pestaña
with steps[1]:
    if st.button('Podemos poner un botón', type = 'primary'):
        texto = st.text_input('¿Cómo le gusta reirse?')
        st.write('usted presionó el botón '+ texto)
    if st.button('Malumita chiquito'):
        st.image('images.jpg', width=30)
        st.image('images.jpg', width=30)

# Agregar una lista de opciones y metricas
with steps[2]:
    st.selectbox('Escoja una opcion', ['Opcion 1', 'Opcion 2', 'Opcion 3'])
    campanhas_df = pd.read_csv('Campanhas.csv', sep = ";")
    camp=st.selectbox('Elija la Campaña', campanhas_df.ID_Campana, 
                 help= "Muestra las campañas existentes")
    
    met_df = pd.read_csv('Metricas.csv', sep = ';')
    m1, m2, m3 = st.columns([1,1,1])

    id1 = met_df[(met_df.ID_Campana == camp)|(met_df.ID_Campana ==1)]
    id2 = met_df[(met_df.ID_Campana == camp)]
    m1.write('Metricas Filtradas')
    m1.metric(label = 'Metrica 1', value = np.sum(id1.Conversiones), 
              delta= str(sum(id1.Rebotes))+' rebotes Totales')

    m2.write('Metricas Filtradas')
    m2.metric(label = 'Metrica 2', value = np.mean(id1.Clics), 
              delta= str(sum(id1.Rebotes))+' rebotes Totales')


# Cargar un dataframe con datos
df=pd.read_csv("https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso1/master/s03/dataVentas2009.csv")
df.Fecha = pd.to_datetime(df.Fecha, format = '%d/%m/%Y')
df.set_index('Fecha', inplace=True)

# Agregar figuras con seaborn
with steps[3]:
    st.dataframe(df)
    varx = st.selectbox('Escoge la variable x', df.columns) 
    fig, ax = plt.subplots()
    ax = sns.histplot(data=df, x = varx)
    # ax.set_xlim(-20,20)  # Fijar el eje x
    st.pyplot(fig)

