import streamlit as st
import requests


st.set_page_config(
    page_title="Rockstar Company",
    page_icon="👾",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.github.com/tezamarlevi',
        'Report a bug': "https://www.google.com/",
        'About': "Hi everybody, let me introduce myself, \
        I am Teza Marlevi Fajar and I am a junior data scientist \
        at Rockstar Automotive Company, on this \
        website I will make app for predict price. \
        This second time make website and i hope you enjoyed it"
    }
)
st.header('Rockstar Automotive')
st.write('Hello everyone, introduce me to Teza Marlevi Fajar, \
a data scientist at a company called Rockstar Automotive Company \
which is located in California, United States of America. \
Rockstar Automotive Company has been established since 2010, \
for 12 years we have always provided convenience to customers \
and now we have a new breakthrough which helps customers to see \
car prices without having to come to our shop, this method is \
very effective because it makes potential buyers not have to \
just come to the store from home and we are the ones who help \
the service.')

st.write("Before you make a car prediction, please enter your identity")
st.text_input('Name')
st.text_input('Email')
st.text_input('Phone Number')

st.write("You can click the 'I want a price prediction' button \
to check the price of the car you want and you will be guided \
until you finish making predictions.")

agree = st.checkbox("I want a car price prediction")
if agree:
    st.title("Car price prediction")
    st.subheader("Brand and Model")
    st.write('In this section, you will choose a brand and a car model that you want to predict')
    col1, col2= st.columns(2)
    with col1:
        brand = st.selectbox("Brand", ['None', 'ford', 'dodge', 'chevrolet', 'gmc', 'chrysler', 'kia',
        'buick', 'infiniti', 'mercedes-benz', 'jeep', 'bmw', 'cadillac',
        'hyundai', 'mazda', 'honda', 'heartland', 'jaguar', 'acura',
        'harley-davidson', 'audi', 'lincoln', 'lexus', 'nissan', 'land',
        'maserati', 'peterbilt', 'ram'])
    with col2:
        model = st.selectbox("Model", ['None','cruiser', 'se', 'mpv', 'door', '1500', 'pk', 'malibu', 'coupe',
        'wagon', 'forte', 'encore', 'sorento', 'doors', 'chassis', 'q70',
        'camaro', 'convertible', 'vans', 'srw', 'compass', 'enclave',
        '300', 'cherokee', 'pacifica', 'x3', 'equinox', 'challenger', 'm',
        'colorado', 'focus', 'durango', 'escape', 'charger', 'explorer',
        'f-150', '3500', 'caravan', 'van', 'dart', '2500', 'esv',
        'cutaway', 'el', 'edge', 'series', 'flex', 'srx', 'cab', 'pickup',
        'vehicl', 'trax', 'tahoe', 'suburban', 'cargo', 'drw', 'fiesta',
        'impala', 'soul', 'elantra', 'pioneer', 'trail', 'traverse',
        'country', 'sundance', 'road/street', 'nautilus', 'gx', 'q5',
        'gle', 'sportage', '5', 'sport', 'discovery', 'acadia', 'ghibli',
        'glc', 'e-class', 'truck', 'utility', 'limited', 'sl-class',
        'cx-3', '2500hd', 'sonic', 'corvette', 'mdx', 'xt5', 'fusion',
        'mustang', 'passenger', 'volt', 'spark', 'cruze', 'ld', 'journey',
        'transit', 'ranger', 'taurus', 'max', 'energi', 'expedition',
        'bus', 'ecosport', 'f-750', 'd', 'dr', 'hybrid', 'suv', 'connect',
        'f-650', 'sentra', 'altima', 'frontier', 'rogue', 'maxima',
        'versa', 'note', 'armada', 'pathfinder', 'titan', 'sedan', 'juke',
        'murano', 'xterra', 'kicks', 'xd', 'nvp'])
    
    st.subheader('Year')
    st.write('In this section you can choose the license year of \
    the car you want, this year starts from 1993 to 2022 if it \
    exceeds that, the price you will get will be different from \
    what it should be.')
    year = st.number_input("Input Year")

    st.subheader("Status")
    st.write("In this section, you will choose between clean vehicle or salvage insurance.")
    title_status = st.selectbox("Select one", ['None','clean vehicle', 'salvage insurance'])

    st.subheader("Mileage")
    st.write('in this section you will choose the distance that has been traveled \
    by the car you have chosen, and keep in mind if the distance you enter is not \
    too similar to the condition that the car we are selling, we will provide the \
    closest distance to the car mileage that you have entered. Max Milegae 1017936')
    mileage = st.number_input("Input Mileage")


    st.subheader("Color")
    st.write("In this section you will choose the color of the car according to \
    your liking, we have many color choices that you can choose according to what \
    you want from the color of your car, if the color of the car is not available \
    we will provide information via email and discuss whether you want a custom \
    color or just choose an available color.")
    color = st.selectbox("Color", ['None','black', 'silver', 'blue', 'red', 'white', 'gray', 'orange',
        'brown', 'gold', 'charcoal', 'turquoise', 'beige',
        'green', 'dark blue', 'maroon', 'phantom black', 'yellow',
        'color:', 'light blue', 'toreador red', 'bright white clearcoat',
        'billet silver metallic clearcoat', 'black clearcoat',
        'jazz blue pearlcoat', 'purple',
        'ruby red metallic tinted clearcoat', 'triple yellow tri-coat',
        'competition orange', 'off-white', 'shadow black',
        'magnetic metallic', 'ingot silver metallic', 'ruby red',
        'royal crimson metallic tinted clearcoat', 'kona blue metallic',
        'oxford white', 'lightning blue', 'ingot silver',
        'white platinum tri-coat metallic', 'guard',
        'tuxedo black metallic', 'tan', 'burgundy', 'super black',
        'cayenne red', 'morningsky blue', 'pearl white', 'glacier white'])

    st.subheader("Country")
    st.write("In this section you will choose a country, this aims to find \
    out if you want to buy a car at the USA or Canada branch")
    country = st.selectbox("Country", ['None','usa', 'canada'])

# inference
    data = {'brand':brand,
            'model': model,
            'year': year,
            'title_status':title_status,
            'mileage':mileage,
            'color':color,
            'country':country}

    # URL = "http://127.0.0.1:5000/predict" # sebelum push backend
    URL = "https://teza-backend.herokuapp.com/predict" # setelah push backend

    # komunikasi
    r = requests.post(URL, json=data)
    res = r.json()

    if r.status_code == 200:
        agree = st.checkbox("Let's see the price")
        if agree:
            st.title(res['result'])
            st.write("This price is in United States Dollars")
            if st.button('Click to buy'):
                st.write('Thank you, we will send information from email')
            else:
                st.write(' ')
    elif r.status_code == 400:
        st.title("ERROR")
        st.write(res['message'])
st.write('  ')      
st.write('  ')
st.write('  ')
st.write('  ')
st.write('  ')
st.write('  ')
slide = st.slider('Rate this website', 0, 5, 0)
if slide == 0 :
    st.caption('swipe to rate')
else :
    st.write('Thank You')

st.write('  ')
title = st.text_input('💬 Commenting app')
if title :
    st.write('Thank you for comment')