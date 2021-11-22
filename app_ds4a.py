import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import json


st.title('Sentiment Analysis of Tweets')
st.sidebar.title('Sentiment Analysis of Tweets')
st.markdown('Dashboard to analyse the sentiment of Tweets 🐦')
st.sidebar.markdown('Dashboard to analyse the sentiment of Tweets 🐦')

data_tweets = ('PROJECT/data_by_caja.csv')
data_menciones = ('PROJECT/out_menciones.csv')
cajas=["cajasan","ComfenalcoAnt","Colsubsidio_Ofi","Compensar_info","comfenalcovalle","CafamOficial"]
def load_data():
    data_t = pd.read_csv('C:/Users/Andres/Desktop/ML/DS4A/PROJECT/data_by_caja.csv')
    data_m = pd.read_csv('C:/Users/Andres/Desktop/ML/DS4A/PROJECT/out_menciones.csv')
    #Just for 6 compensation funds this will be deleted
    cajas=["cajasan","ComfenalcoAnt","Colsubsidio_Ofi","Compensar_info","comfenalcovalle","CafamOficial"]
    data = pd.merge(data_t,data_m, on=['id_str'], how='inner')
    data = data[data.screen_name.isin(cajas)]
    data['tweet created'] = pd.to_datetime(data['created_at'])
    data=data.rename(columns={'screen_name': "Caja"})
    return data

data = load_data()

st.sidebar.subheader('Show random tweet')
random_tweet = st.sidebar.radio('Sentiment',('Very positive','Positive','Neutral','Negative','Very negative'))
## Add functionality return one random tweet according to selected sentiment #iat function used to access specifically the text
# and not the dataframe position
st.sidebar.markdown(data.query('label_polarity==@random_tweet')[['full_text']].sample(n=1).iat[0,0][0:200])

st.sidebar.markdown('### Number of tweets by sentiment')
#Key parameter is used to specify the acction and not be confused with other functionality
select = st.sidebar.selectbox('Visualization type',['Histogram','Pie chart'],key='1')
sentiment_count = data['label_polarity'].value_counts()

sentiment_count = pd.DataFrame({'Sentiment':sentiment_count.index,'Tweets':sentiment_count.values})

if not st.sidebar.checkbox('Hide',True):
    st.markdown('### Number of tweets by sentiment')
    if select =='Histogram':
        fig = px.bar(sentiment_count,x='Sentiment',y='Tweets',color='Tweets',height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count,values='Tweets',names='Sentiment')
        st.plotly_chart(fig)

# Sentiment for each compensation fund :)
st.sidebar.subheader('Breakdown compensation funds tweets by sentiment')
choice = st.sidebar.multiselect('Pick compensation fund',("cajasan","ComfenalcoAnt","Colsubsidio_Ofi","Compensar_info","comfenalcovalle","CafamOficial"),key='0')
if len(choice)>0:
    choice_data = data[data.Caja.isin(choice)]
    fig_choice = px.histogram(choice_data,x='Caja',y='label_polarity',histfunc='count',color='label_polarity',
    facet_col='label_polarity',labels ={'label_polarity':'tweets'},height=600,width=800)
    st.plotly_chart(fig_choice)

## Word Clouds for each compensation fund

st.sidebar.header('Word Cloud')
word_sentiment = st.sidebar.radio('Display word cloud for which sentiment',('Very positive','Positive','Neutral',
'Negative','Very negative'))

##Stopwords
ruta = ('C:/Users/Andres/Desktop/ML/DS4A/PROJECT/stopwords.json')
with open(ruta, 'r') as f:
    datastore = json.load(f)
stop_words = datastore['words']


if not st.sidebar.checkbox('Hide',True,key='3'):
    st.header('Word cloud for %s sentiment'%(word_sentiment))
    df = data[data['label_polarity']==word_sentiment]
    words = ' '.join(df['plain_text'])
    processed_words =' '.join([word for word in words.split() if 'http'not in word and not word.startswith('@')])
    wordcloud = WordCloud(stopwords=stop_words,background_color = 'white',height=640,width=800).generate(processed_words)
    plt.imshow(wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()

