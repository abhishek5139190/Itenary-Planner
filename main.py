from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating a travel itinerary

travel_template = "I am travelling from {city_1} to {city_2}  generate me a {day} days travel itenary along with travel plan like how i can reach this {city_2} from {city_1} and places to visit"


travel_prompt = PromptTemplate(template = travel_template, input_variables = ['city_1', 'city_2', 'day'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-thinking-exp-01-21")


# Create LLM chain using the prompt template and model
travel_chain = travel_prompt | gemini_model


import streamlit as st

st.header("Travel Itenary Creator")

st.subheader("Your Personal Travel Itenary Generator ")

city_1 = st.text_input("From City")
city_2 = st.text_input("To City")

day = st.number_input("Number of days", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Create"):
    travel = travel_chain.invoke({"city_1" : city_1, "city_2" : city_2, "day" : day})
    st.write(travel.content)
    
