import streamlit as st
import pandas as pd

#Create Title
st.title("Hello Streamlit")

st.write("This is a simple page")

## Create simple dataframe
df = pd.DataFrame({

    'first column':[1,2,3,4],
    'second column':[10,20,30,40]

})


#Displaying Dataframe:
st.write("Here is the dataframe")
st.write(df)