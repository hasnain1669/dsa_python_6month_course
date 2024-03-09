import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np

# Load the datasets
tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')
iris = sns.load_dataset('iris')
diamonds = sns.load_dataset('diamonds')

# User-defined dataset
# Replace 'your_dataset.csv' with the path to your own dataset
your_dataset = pd.read_csv(input('upload your dataset here:'))

# Sidebar selection
dataset = st.sidebar.selectbox('Select Dataset', ('Tips', 'Titanic', 'Iris', 'Diamonds', 'your_dataset'))

# Display the selected dataset
if dataset == 'Tips':
    st.dataframe(tips)
elif dataset == 'Titanic':
    st.dataframe(titanic)
elif dataset == 'Iris':
    st.dataframe(iris)
elif dataset == 'Diamonds':
    st.dataframe(diamonds)
elif dataset == 'Your Dataset':
    st.dataframe(your_dataset)

# Perform EDA on the selected dataset
# Add your EDA code here

# Run the app
if __name__ == '__main__':
    st.title('Exploratory Data Analysis App')
    st.write('Select a dataset from the sidebar to perform EDA.')