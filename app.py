# -*- coding: utf-8 -*-


"""
@author: Fascilla Gianfranco
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import pandas #as pd
import pickle
import streamlit as st
from PIL import Image
#primaryColor="#F63366"
#backgroundColor="#FFFFFF"
model = pickle.load(open('streamlit.pk','rb'))
@st.cache
def predict(Gender, Age, Height, Weight, Duration, Heart_Rate,Body_Temp):
    prediction = model.predict(pandas.DataFrame([[Gender, Age, Height, Weight, Duration,Heart_Rate,Body_Temp]], columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate','Body_Temp']))
    prediction=abs(prediction)
    return prediction
image = Image.open('dottore_small2.png')
image2= Image.open('allenamento2.jpg')
image3 = Image.open('pasticcini3.jpg')
image4= Image.open('donna.JPG')
image4=image4.resize((300,200))
image5 = Image.open('uomo.JPG')
image5= image5.resize((300,200))
#st.image(image2)
#st.image(image)
st.header('..........Calcolo KCalorie consumate .........')
#st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.sidebar.image(image2)
st.sidebar.info('questa app e^ stata creata per conoscere le Kcalorie consumate dopo un esercizio fisico(corsa,ecc.ecc)')
st.sidebar.info('                Created by Fascilla Gianfranco(Kaggle competitor)')
st.sidebar.info('Le specifiche del modello di calcolo solo su^ richiesta')
st.sidebar.success('gianfranco.fa@gmail.com')
#st.header('     Immetti i dati:')
#st.header('      attenzione digita in Gender 0 =Donna  1= Uomo')
#st.header('Duration=durata esercizio fisico in minuti')
#st.header('Body_Temp=temperatura corporea a fine esercizio')
#st.header('Heart_Rate=battito cardiaco a fine esercizio')
st.header('il calcolo viene eseguito con una rete neurale  addestrata su 15000 dati clinici')
#st.header('     Immetti i dati:')
st.subheader('seleziona Sesso...   DONNA = 0 ... UOMO = 1')
Gender = st.slider("SESSO: ", min_value=0,   
                       max_value=1, value=1)
if Gender==0:
    st.subheader('hai selezionato DONNA')
else:
    st.subheader('hai selezionato UOMO')
if Gender==0:
    st.image(image4)
else:
    st.image(image5)
#Gender = st.number_input('Gender:', min_value=0.0, max_value=1.0,value=1.0)
#Gender = st.multi_select("seleziona sesso",["0","1"])
st.subheader('inserisci eta^')
Age = st.number_input('Age:', min_value=18.0,max_value=75.0,value=18.0)
st.subheader('inserisci altezza in centimetri')
Height = st.number_input('Height:', min_value=125.0,max_value=210.0,value=125.0)
st.write('inserisci peso in kg (reale please)')
Weight = st.number_input('Weight:', min_value=40.0,max_value=160.0,value=40.0)
st.subheader('inserisci durata esercizio(corsa ecc ecc) in minuti')         
Duration = st.number_input('Duration:', min_value=10.0, max_value=240.0, value=10.0)
st.subheader('inserisci battito cardiaco a fine esercizio')         
Heart_Rate = st.number_input('Heart_Rate:', min_value=65.0,max_value=230.0,value=65.0)
st.subheader('inserisci temperatura corporea a fine esercizio se^ non puoi inserisci 37 ')         
Body_Temp = st.number_input('Body_Temp:', min_value=36.0,max_value=41.0,value=36.0)
st.markdown(
    """
    <style>
    textarea {
        font-size: 2rem !important;
    }
    input {
        font-size: 2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#tolleranza=(Calorie_Bruciate*3)/100
if st.button('Calcolo Calorie'):
    Calorie_Bruciate = predict(Gender, Age, Height, Weight, Duration, Heart_Rate,Body_Temp)
    tolleranza=(Calorie_Bruciate*3)/100
    #st.subheader(f' calcolo Kcalorie ... tolleranza... 5% ..   {Calorie_Bruciate[0]:.2f} KCAL')   #### originale ###
    st.subheader(f' calcolo Kcalorie .....   {Calorie_Bruciate[0]:.2f} KCAL') 
    st.subheader(f' con tolleranza.....di... {tolleranza[0]:.0f} KCAL')  
    #st.header(f' calcolo Kcalorie....
    #if Calorie_Bruciate<=300:
       #st.header('.........SFORZATI UN PO^ DI PIU^')
       #st.header('QUESTI LI VEDI SOLO a NATALE')
       #st.image(image3) 
    #elif Calorie_Bruciate<450:
        #st.header('........PUOI FARE DI MEGLIO')
    #else:
        #st.header('........OTTIMO LAVORO COMPLIMENTI')
        #st.header('PUOI PERMETTERTI QUESTI OGNI TANTO')
        #st.image(image3)
#st.image(image)    

