## Save tokenizer
with open('/content/drive/My Drive/DS4A Project (1)/Tweets_Clasificados/tokenizer.sav', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

## Load tokenizer
with open('tokenizer.sav', 'rb') as handle:
    test_tokenizer = pickle.load(handle)

## Save model
model_sentimiento.save('/content/drive/My Drive/DS4A Project (1)/Tweets_Clasificados/model_sentimiento.sav')

## Load the model
new_model = tf.keras.models.load_model('model_sentimiento.sav')


## Codigo para predecir sentimiento

# 1. Cargar modelo

# 2. Cargar Tokenizer

# 3. Predict para cada tweet

# Ejemplo
max_length = 60
#Tweet de entrada
tweet = 'Pesimo serivicio los odio miserables'
#convertir en series
t_f = pd.Series(tweet)
##Apply tokenizer
sec = tokenizer.texts_to_sequences(t_f)
##padding input del modelo
pad = pad_sequences(sec,maxlen=max_length)
# Predicción if sen<0.5 ==> Negativo
            #if sen>0.5 ==>Positivo 
classes = model_sentimiento.predict(pad)



## Codigo Clasificar Servicios

## Considerar que las categorias corresponden a: 
# (0:Cultura, 1:General, 2:Otros, 3:Salud, 4:Subsidios)
max_length = 60
## Mismo proceso tokenizer, secuencia, padding
test_s = 'Realice la apelación por el subsidio de emergencia a @CafamOficial ya voy para un mes esperando respuesta cuando se supone eran 10 días habiles. El mismo día me comunique con @Supersubsidio quiénes ya me dieron respuesta y me indican que si cumplo con todos los requisitos.'
t = pd.Series(test_s)
t_sec = tokenizer.texts_to_sequences(t)
## Input del modelo 
t_pad = pad_sequences(t_sec,maxlen=max_length)
## Prediccion
classes = model_servicio.predict(t_pad)
## El servicio al que pertenece el tweet consiste en la posicion del elemento con mayor probabilidad
## es decir el argumento maximo
p_c = np.argmax(classes)
##Codigo para definir el servicio al que pertenece el tweet 
if p_c==0:
  print('Servicio:Cultura')
elif p_c==1:
  print('Servicio:General')
elif p_c==2:
  print('Servicio:Otros')
elif p_c==3:
  print('Servicio:Salud')
else:
  print('Servicio: Subsidio')


## Correr modelo en batch
max_length = 60
test_sentences = #set de tweets descargados
#test_sentces debe estar en formato pandas.core.series.Series
testing_sequences = tokenizer.texts_to_sequences(test_sentences)
testing_padded = pad_sequences(testing_sequences,maxlen=max_length)

for t in testing_padded:
    pred = model_servicio.predict(t)
    serv = np.argmax(pred)
    if p_c==0:
        #Accion que se desee, añadir a una columna de servicio......
        print('Servicio:Cultura')
    elif p_c==1:
        print('Servicio:General')
    elif p_c==2:
        print('Servicio:Otros')
    elif p_c==3:
        print('Servicio:Salud')
    else:
        print('Servicio: Subsidio')
    


