# NLP-for-pulbic-perception-evaluation
Public perception of the Colombian compensation funds

The superintendency of family subsidy is a Colombian entity in charge of supervising the
family subsidy system, specifically the family compensation funds, which offers different
services of education, recreation, health, tourism and subsidies among others. The
superindency wants to know and understand the users feeling and perception of each fund,
in order to improve the customer service and general perception.
To solve this, we took the information from Twitter of the funds, due to is a very important
network and the information is public. The model extract all the Tweets related to the funds
each 6 hours and save them in a database, where are processed each 5 minutes in groups
of 500 tweets.
We create a LSTM recursive neural network model customized and trained in our language
(the model was trained with a manual classification to identify local language), that classifies
each Tweet into positive or negative feeling, in addition, the model classify the service of
which each tweet refers grouped in health, subsides, general, culture and others.
The information is displayed in a dashboard, in which in real time and dynamically the user
can filter by compensation fund, service and dates, and see the sentiment analysis, the word
cloud with the most common words and the amount of tweets per day and hour.

