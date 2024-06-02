# import libraires
import streamlit as st
import plotly.express as px
import pandas as pd

# import dataset
st.title ('Plottling with Plotly and Streamlit')
df = px.data.gapminder()
st.write(df)

st.write(df.columns)

# summary statistics

st.write(df.describe())

# data management in streamlit

year_option = df['year'].unique().tolist()

year = st.selectbox("Which year would you liked to plot?", year_option, 0)

# df = df[df['year']==year]

fig = px.scatter(df, x = 'gdpPercap', y = 'lifeExp', size = 'pop', color = 'country', hover_name = 'country',
                 log_x = True, size_max = 60, range_x= [100, 100000], range_y = [20, 90])

fig.update_layout(width=800, height=400)
st.write(fig)

fig = px.scatter(df, x = 'gdpPercap', y = 'lifeExp', size = 'pop', color = 'continent', hover_name = 'continent',
                 log_x = True, size_max = 60, range_x= [100, 100000], range_y = [20, 90],
                 animation_frame='year', animation_group='country')

fig.update_layout(width=800, height=400)
st.write(fig)