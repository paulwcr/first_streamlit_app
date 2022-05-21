import streamlit
streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu:')
streamlit.text('🥣 Omega 3 & blubeberry oatmeal')
streamlit.text('🥗Kale, spinach & rocket smoothie')
streamlit.text('🐔 Hard-boiled free-range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("pick some fruits: ", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
 
streamlit.dataframe(fruits_to_show)

# New section to display the Fruity Vice API resonse
streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #just writes the data to the screen

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)
