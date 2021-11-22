st.sidebar.subheader('Show random tweet')
random_tweet = st.sidebar.radio('Sentiment',('Very positive','Positive','Neutral','Negative','Very negative'))
## Add functionality return one random tweet according to selected sentiment #iat function used to access specifically the text
# and not the dataframe position
st.sidebar.markdown(data.query('label_polarity==@random_tweet')[['full_text']].sample(n=1).iat[0,0][0:200])