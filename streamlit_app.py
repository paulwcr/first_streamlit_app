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
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The User entered', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen
#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector;

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains: ")
streamlit.dataframe(my_data_rows)

#allow the end user to add another fruit to the list 
add_my_fruit = streamlit.text_input('What fruit would you like to add', 'jackfruit')
streamlit.write('Second fruit is:', add_my_fruit)
import requests
fruityvice_response2 = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen
#take the json version of the response and normalize it
fruityvice_normalized2 = pandas.json_normalize(fruityvice_response2.json())
#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized2)
