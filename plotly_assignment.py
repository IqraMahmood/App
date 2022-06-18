print("Name: Iqra Mahmood")
print("Email: Iqramultaji@gmail.com")

import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

st.title("App with Plotly and Streamlit ")

df = sns.load_dataset('titanic')
df = df.dropna()
st.subheader("Dataset")
st.write(df)
st.write(df.head())
st.subheader("Dataset columns")
st.write(df.columns)

# SUMMARY STAT
st.subheader(" Description Summary")
st.write(df.describe())

# Data Managment
st.subheader("Genderr selection")
year_option = df['sex'].unique().tolist()
sex = st.selectbox("Which gender should we plot ?",year_option, 0)
# df = df[df['sex'] == sex]

# Plotting
st.subheader("Plotting")
fig = px.scatter(df, x = 'pclass', y = 'fare',size = 'age',color = 'class', hover_name = 'class',
log_x=True, size_max=55,range_x=[.5,10], range_y=[1,550],animation_frame='sex',animation_group='class')

fig.update_layout(width = 600, height = 400)
st.write(fig)

