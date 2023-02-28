import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Cheers to the New Beginnings!')

streamlit.header('Start reading Fruits using Pandas :) !')

# call the read_csv function
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect('Pick some fruits:',list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Use streamlit dataframe to call the my_fruit_list object
# streamlit.dataframe(my_fruit_list)

# Put a pick-list to select the fruit to include
# iteration 2: added selections in the square brackets to indicate the pre-populated list
# iteration 3: show only the selected fruits on the streamlit dataframe
# streamlit.multiselect('Pick some fruits:',list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(fruits_to_show)

# new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
#normalizing the incoming json data for the api endpoint
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output in screen as table
#streamlit.dataframe(fruityvice_normalized)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output in screen as table
#streamlit.dataframe(fruityvice_normalized)

try:
  fruit_choice = streamlit.text_input('What Fruit would you like information about?')
  if not fruit_choice:
      streamlit.error('Please select a fruit for information')
  else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()

streamlit.stop() 

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
#streamlit.text("Fruit Load List contains:")
streamlit.header("Fruit Load List contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What Fruit would you like to add?','Jackfruit')
#streamlit.write('The user entered', add_my_fruit)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)

streamlit.write('The user entered', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
