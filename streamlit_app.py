import streamlit

streamlit.title('Cheers to the New Beginnings!')

streamlit.header('Start reading Fruits using Pandas :) !')

# import pandas
import pandas
# call the read_csv function
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Use streamlit dataframe to call the my_fruit_list object
streamlit.dataframe(my_fruit_list)

# Put a pick-list to select the fruit to include
streamlit.multiselect('Pick some fruits:',list(my_fruit_list.index))

