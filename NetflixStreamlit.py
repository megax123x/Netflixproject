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
rad=st.sidebar.radio("Navigation",['MORE PROJECT','DATA EXPLORE', 'TOP 10', 'RECOMANDATION SYSTEM'])


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

    st.image('https://raw.githubusercontent.com/megax123x/Netflixproject/main/sunrise.jpg', caption='Sunrise In la creuse')

# Creat an expander to memorize the data set selected
expander = st.sidebar.beta_expander("SELECTED DATA")
expander.markdown(
    """
    The only selected movie are the one distributed in france. 
    Netflix exlusive movie will be deleted from the database to answer client quiers.
    Information may varie, please check the time line.
    """)

expander.info(' Wild code school project 03/05/2020')

#Creat a data set because it was hard to load
data1={
    "Name":['title_principals','title_basics','title_akas','title_crew','title_episode','name_basics','title_ratings'],
    "Column":[43998946,7783583,25827064,7780369,5663721,10838773,1136817],
    "Number of rows":[6,9,8,3,4,6,3],
}
df=pd.DataFrame(data=data1)


if rad=='DATA EXPLORE':
    st.title("Choissiez une base de donnée pour l'examiner")
    st.title("")
    agree = st.checkbox('All table')
    if agree:
        st.markdown("""
        In this notebook, we will explore IMDb’s dataset which is available online.
        https://www.imdb.com/interfaces/
        it has  seven tables at total
        """)
        fig = px.bar(df, x="Name", y="Number of rows",title='<b>Table content', color_discrete_sequence=['coral'])
        fig.update_yaxes(title=None, tick0=True, nticks=12)
        fig.update_xaxes(title=None, nticks=12)
        fig.update_layout(showlegend=False, font_family='IBM Plex Sans',margin=dict(l=30, r=30, b=30))
        st.plotly_chart(fig, use_container_width=True)


#Create a select box to show content of each table

    option = st.selectbox('', ('title_principals','title_basics','title_akas','title_crew','title_episode','name_basics','title_ratings'))

    if option=='title_principals':
         df.iloc[0]
         st.markdown("""
         Over 43 million lines, the table has 
         coming from different professions such as actors, 
         actresses, directors, writers, etc. 
         It contains their birth and death year info as well as their most known work of art.
         """)
         
        
    if option=='title_basics':
         df.iloc[1]
         st.write('the most important table')

    if option=='title_akas':
         df.iloc[2]
         st.markdown("""
         contains the information about the movies , like primary type, adult or not, end year, runningtime, and genre.
         """)
    
    if option=='title_crew':
         df.iloc[3]
         st.write("Contains the director and writer information for all the titles in IMDb.")
    
    if option=='title_episode':
         df.iloc[4]
         st.write('Not relevant for our analysis.we are only interested in movies in the notebook, not TV series.')

    if option=='name_basics':
         df.iloc[5]
         st.markdown("""
         Contains the following information for prople names like birthyear, deathyear,...
         """)

    if option=='title_ratings':
         df.iloc[6]
         st.markdown("""
         Contains the IMDb rating and votes information for titles
         """)

    ### second


if rad=='TOP 10':
     st.title('TOP 10 per year')
     st.header('the data base inclued only movies distrubuted in france with a rating of 7+ and 1500 vote ')
     dfml=pd.read_csv('https://raw.githubusercontent.com/megax123x/Netflixproject/main/dfml.csv')
     listedate=dfml['startYear'].to_list()
     Yearlist=list(set(listedate))
     st.title('')
     option_date=st.selectbox('Chosse a year',(Yearlist))
     
     for dateItem in Yearlist:
          if option_date==dateItem:
               st.write('**By avreage rating**')
               Df_Top10_movies_Rating=dfml[['title','startYear','averageRating','genres', 'primaryName']][dfml['startYear']==dateItem ].sort_values(by='averageRating', ascending=False)
               Df_Top10_movies_Rating.iloc[0:10]
               st.markdown("""**By numVotes**""")
               Df_Top10_movies_Rating=dfml[['title','startYear','numVotes','genres']][dfml['startYear']==dateItem ].sort_values(by='numVotes', ascending=False)
               Df_Top10_movies_Rating.iloc[0:10] 
