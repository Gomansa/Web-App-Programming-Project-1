import streamlit as st
import json
import requests
import nltk
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

import main_functions

api_key_dict = main_functions.read_from_file("JSON_Files/api_key.json")
api_key = api_key_dict["my_key"]

url = "https://api.nytimes.com/svc/topstories/v2/travel.json?api-key=" + api_key

st.title("COP4813 - Web Application Programming")
st.title("Project #1")

st.header("Part A")
st.subheader("This app used the Top Stories API to display the most common words used in the top current articles based on a specified topic "
             "selected by the user. The data is displayed as a line chart and as a wordcloud image.")

st.header("I - Topic Selection")
name = ""
user_input = st.text_input("Please enter your name", name)
option = st.selectbox("Please select a topic",
                      ["","arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider",
                       "magazine", "movies", "nyregion", "obituaries", "opinion", "politics",
                       "realestate", "science", "sports", "sundayreview", "technology", "theater",
                       "t-magazine", "travel", "upshot", "us", "world"])

st.write("Hi ", user_input, ", you selected the ", option, " topic.")

st.header("II - Frequency Distribution")
#option2 = st.selectbox("Click here to generate frequency distribution")


