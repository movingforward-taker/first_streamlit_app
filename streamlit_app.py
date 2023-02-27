import streamlit

streamlit.title('Cheers to the New Beginnings!')

streamlit.header('Start reading Fruits using Pandas :) !')

# import pandas
import pandas
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
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
#normalizing the incoming json data for the api endpoint
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output in screen as table
#streamlit.dataframe(fruityvice_normalized)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output in screen as table
streamlit.dataframe(fruityvice_normalized)

