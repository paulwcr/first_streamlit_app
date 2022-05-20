import streamlit
streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu:')
streamlit.text('🥣 Omega 3 & blubeberry oatmeal')
streamlit.text('🥗Kale, spinach & rocket smoothie')
streamlit.text('🐔 Hard-boiled free-range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
