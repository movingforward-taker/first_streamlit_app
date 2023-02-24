import streamlit

streamlit.title('Cheers to the New Beginnings!')

streamlit.header('Stop the mundane activities!')
streamlit.text('Work on fitness goals')
streamlit.text('Continue on your passion')
streamlit.text('Stay true to your conscience')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
