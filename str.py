import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def get_data():
    return []

user_id = st.text_input("User ID")
Name = st.text_input("What\'s your name?")
foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)

if st.button("Submit"):
    get_data().append({"UserID": user_id,"Name":Name, "foo": foo, "bar": bar})

st.write(pd.DataFrame(get_data()))
A=pd.DataFrame(get_data())
A.to_excel('Vic.xlsx')
