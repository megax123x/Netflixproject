import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import plotly.express as px
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import preprocessing



#Creat a side bar really useful at the start of the project
rad=st.sidebar.radio("Navigation",['MORE PROJECT','DATA EXPLORE', 'Netoyage de la base', 'Machine learning'])


### first introduction
   
if rad=='MORE PROJECT':

    st.title('Build a movies recomandation system.')
    st.subheader('Equipe projet:Michael, Raph, Fanym, Ahlem, Soufiane')
    st.title(" ")
    st.markdown("""
        We at the wild code school we value the time of our customers. 
        We know how much you like to expand your dream, shatter your expecation, drive into a story, on watching movies.
        I mean we all love movies.
        We decided to help you and propose the best movie ever created.
        Our recomandation system, is a powerful tool which will help you to enjoy the best movies and recommand to you the one to watch based on your preference
        At the end of this anylses all you have to do is to chose one favorite movie, we all have one, and base your selection, you will be amzed how much the thetre univers is filled with movies wiating for you to love.
        :tada:
        """)
    st.title(" ")
    st.subheader('Enjoy!')

    st.image('https://github.com/megax123x/Netflixproject/blob/main/sunrise.jpg', caption='Sunrise In la creuse')

# Creat an expander to memorize the data set selected
expander = st.sidebar.beta_expander("Data selected")
expander.markdown(
    """
    The only selected movie are the one distributed in france. Netflix exlusive movie will be deleted from the data base to answer ro client quiers
    Information may varie, please check the time line
    """)

expander.info('03/05/2020')

#Creat a data set because it was hard to load
data1={
    "Nom":['La table name basics','La table Title', 'La table Title basics', ' La tables crew', 'La table episode','La table Title episode','La table title Principal'],
    "Nombre de colonnes":[6,9,8,3,4, 6,3],
    "Total de lignes":[43998946, 7783582, 25827063, 7780368, 5663720, 10838772, 1136817],
}
df=pd.DataFrame(data=data1)


if rad=='DATA EXPLORE':
    st.title("Choissiez une base de donnée pour l'examiner")
    st.title("")
    agree = st.checkbox('All table')
    if agree:
        st.markdown("""
        In this notebook, we will explore IMDb’s dataset which is available online and refreshed daily.
        https://www.imdb.com/interfaces/
        it has  seven tables at total
        """)
        fig, ax = plt.subplots(figsize=(15,10)) 
        ax=sns.barplot(x="Nom", y="Total de lignes", data=df)
        st.pyplot(fig)

    option = st.selectbox('', ('La table name basics','La table Title', 'La table Title basics', ' La tables crew', 'La table episode','La table Title episode','La table title Principal'))

    if option=='La table name basics':
         df.iloc[0]
        
    if option=='La table Title':
         df.iloc[1]

    if option=='La table Title basics':
         df.iloc[2]
    
    if option==' La tables crew':
         df.iloc[3]
    
    if option=='La table episode':
         df.iloc[4]

    if option=='La table Title episode':
         df.iloc[5]

    if option=='La table title Principal':
         df.iloc[6]

    ### second
