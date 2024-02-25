import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns

# adding title of the app
st.title('Grocery Store')

# Adding simple text
st.write('Welcome to the Grocery Store, Today we have a special offer for you, Try it after your shopping')

# adding userinput with slider with range step 1000
amount = st.slider('How much amount did you pay for the grocery?', 0, 100000, 1000)

# print the text of number
st.write('You paid:', amount)

# adding a button as click me if the amount greater then 5000 then you won 500 points
if st.button('Try your luck'):
    if amount > 80000:
        st.write('You won 8000 points')
    elif amount >= 60000 and amount <= 80000:
        st.write('You won 6000 points')
    elif amount >= 50000 and amount <= 60000:
        st.write('You won 5000 points')
    elif amount >= 30000 and amount <= 50000:
        st.write('You won 3000 points')
    elif amount >= 10000 and amount <= 30000:
        st.write('You won 1000 points')
    elif amount >= 5000 and amount <= 10000:
        st.write('You won 500 points')
    else:
        st.write('You won 100 points')
else:
    st.write('Try again')

# adding a text as farewell
st.write('Thanks for Shooping with us, Goodbye')

# adding radio button with options
weekdays = st.radio(
        'On which day did you do grocery?',
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )

# print the selected day
st.write('You did grocery on:', weekdays)

# adding sidebar with selectbox
st.sidebar.write('Contact Information')
# adding a selectbox in sidebar with options
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# adding a text input in sidebar    
st.sidebar.text_input('Your Contact Information:', option)

# adding a uploader to upload the file in the sidebar
uploaded_file = st.sidebar.file_uploader('Add you grocery bill here', type='jpg')

# show the uploaded file
if uploaded_file is not None:
    st.sidebar.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

# adding a text input in the main page, to get the user name, and max length, 
name = st.text_input('Enter your name:', max_chars=30)

# adding the address input with placeholder
address = st.text_area('Enter your address:', max_chars=100)

# adding a button to submit the form
if st.button('Submit'):
    st.write('Thanks for submitting the form')

# adding a checkbox to agree the terms and conditions
agree = st.checkbox('I agree to the Terms and Conditions')
