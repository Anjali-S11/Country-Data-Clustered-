
import streamlit as st
import pickle
import pyforest

## load the instances that were created

with open('final_model.pkl','rb') as file:
    model = pickle.load(file)

with open('pca.pkl','rb') as file:
    pca = pickle.load(file)
    
with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)

def prediction(input_data):
    
    scaled_data = scaler.transform(input_data)
    pca_data = pca.transform(scaled_data)
    pred = model.predict(pca_data)[0]

    if pred==0:
        return 'Developing'
    elif pred==1:
        return 'Underdeveloped'
    else:
        return 'Developed'

def main():
    st.title('HELP International Foundation')
    st.subheader('This application will give the status of the country based on the socio-economic factors')
    ch_mort = st.text_input('Enter the child mortality rate:')
    exp = st.text_input('Enter Exports (% GDP):')
    hel = st.text_input('Enter expenditure on health (% GDP):')
    imp = st.text_input('Enter Imports (% GDP):')
    inc = st.text_input('Enter average income:')
    inf = st.text_input('Enter inflation:')
    life_exp = st.text_input('Enter life expectancy:')
    fer = st.text_input('Enter fertility rate:')
    gdpp = st.text_input('Enter GDP per population:')

    input_list = [[ch_mort , exp , hel ,imp,inc,inf,life_exp,fer,gdpp]]
    
    if st.button('Predict'):
        response = prediction(input_list)
        st.success(response)
if _name_== '_main_':
    main()