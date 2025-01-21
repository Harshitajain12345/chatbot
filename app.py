import streamlit as st
from dotenv import load_dotenv 
load_dotenv()
import google.generativeai as genai

import os
google_api_key = os.getenv("GOOGLE_API_KEY")

def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title='chatbot for Q&A')
st.header('chatbot for Q&A by hj')
st.header('chatbot for Q&A by hj')


input = st.text_input("Input :" ,key = "input")

submit = st.button("Get Response!")

if submit:
    response = get_gemini_response(input)
    st.subheader("the response is:")
    st.write(response)





