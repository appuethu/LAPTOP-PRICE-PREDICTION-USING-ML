import streamlit as st 
import pandas as pd
import pickle

st.title("Laptop Price Prediction")

Company=st.radio("Enter the Company",['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI',
       'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer',
       'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'])
TypeName=st.radio("Pick Your TypeName",['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible',
       'Workstation', 'Netbook'])
Ram=st.number_input("Select the Ram")
Weight=st.number_input('Select the Weight')
Touchscreen=st.number_input("Enter the Touchscreen")
Ips=st.number_input("Enter the Ips")
ppi=st.number_input("Enter ppi")
Cpubrand=st.radio("Enter Cpu brand",['Intel Core i5', 'Intel Core i7', 'AMD Processor', 'Intel Core i3',
       'Other Intel Processor'])
HDD=st.number_input("Select the HDD")
SSD=st.number_input("Select the SSD")
Hybrid=st.number_input("Select the Hybrid")
Flash_Storage=st.number_input("Select the Flash_Storage")
Gpubrand=st.radio("Enter Gpu brand",['Intel', 'AMD', 'Nvidia'])
submit=st.button("Submit")

with open('modellinear.pkl', 'rb') as file:  
    model = pickle.load(file)

if submit==True:
    if Company=='LG':
        Company=18
    if Company=='Fujitsu':
        Company=17
    if Company=='Google':
        Company=16
    if Company=='Samsung':
        Company=16
    if Company=='Mediacom':
        Company=15
    if Company=='Razer':
        Company=14
    if Company=='Vero':
        Company=13
    if Company=='Xiaomi':
        Company=12
    if Company=='Huawei':
        Company=11
    if Company=='Toshiba':
        Company=10
    if Company=='Microsoft':
        Company=9
    if Company=='MSI':
        Company=8
    if Company=='Chuwi':
        Company=7
    if Company=='Lenovo':
        Company=6
    if Company=='Dell':
        Company=5
    if Company=='Asus':
        Company=4
    if Company=='Acer':
        Company=3
    if Company=='HP':
        Company=2
    if Company=='Apple':
        Company=1
    
    
    if TypeName=='Netbook':
        TypeName=5
    if TypeName=='Workstation':
        TypeName=5
    if TypeName=='2 in 1 Convertible':
        TypeName=4
    if TypeName=='Gaming':
        TypeName=3
    if TypeName=='Notebook':
        TypeName=2
    if TypeName=='Ultrabook':
        TypeName=1
    
    
    if Cpubrand=='Other Intel Processor':
        Cpubrand=5
    if Cpubrand=='Intel Core i3':
        Cpubrand=4
    if Cpubrand=='AMD Processor':
        Cpubrand=3
    if Cpubrand=='Intel Core i7':
        Cpubrand=2
    if Cpubrand=='Intel Core i5':
        Cpubrand=1
        
    if Gpubrand=='Nvidia':
        Gpubrand=3
    if Gpubrand=='AMD':
        Gpubrand=2
    if Gpubrand=='Intel':
        Gpubrand=1
    
    
    
    prediction_data=pd.DataFrame({
        'Company':[Company],
        'TypeName':[TypeName],
        'Ram':[Ram],
        'Weight':[Weight],
        'Touchscreen':[Touchscreen],
        'Ips':[Ips],
        'ppi':[ppi],
        'Cpu brand':[Cpubrand],
        'HDD':[HDD],
        'SSD':[SSD],
        'Hybrid':[Hybrid],
        'Flash_Storage':[Flash_Storage],
        'Gpu brand':[Gpubrand]
        
    })
    
    prediction=model.predict(prediction_data)

    st.text_area('Result',prediction)