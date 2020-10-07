import streamlit as st
import wordcloud
import matplotlib.pyplot as plt
import requests
import main_functions
import pandas as pd
import plotly.express as px
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud

api_key_dict = main_functions.read_from_file("JSON_Files/api_key.json")
api_key = api_key_dict["my_key"]

# url = "https://api.nytimes.com/svc/topstories/v2/travel.json?api-key=" + api_key

st.title("COP4813 - Web Application Programming")
st.title("Project #1")

st.header("Part A")
st.subheader(
    "This app used the Top Stories API to display the most common words used in the top current articles based on a "
    "specified topic selected by the user. The data is displayed as a line chart and as a wordcloud image.")

st.header("I - Topic Selection")
user_input = st.text_input("Please enter your name")
option = st.selectbox("Please select a topic",
                      ["", "arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider",
                       "magazine", "movies", "nyregion", "obituaries", "opinion", "politics",
                       "realestate", "science", "sports", "sundayreview", "technology", "theater",
                       "t-magazine", "travel", "upshot", "us", "world"])

if user_input and option:
    st.write("Hi " + user_input + ", you selected the " + option + " topic.")

    st.header("II - Frequency Distribution")

    agree = st.checkbox("Click here to generate frequency distribution.")
    if agree:

        new_url = "https://api.nytimes.com/svc/topstories/v2/" + option + ".json?api-key=" + api_key

        response = requests.get(new_url).json()
        main_functions.save_to_file(response, "JSON_Files/response.json")

        my_articles = main_functions.read_from_file("JSON_Files/response.json")

        str1 = ""

        for i in my_articles["results"]:
            str1 = str1 + i["abstract"]

        # sentences = sent_tokenize(str1)
        words = word_tokenize(str1)
        fdist = FreqDist(words)
        words_no_punc = []

        for w in words:
            if w.isalpha():
                words_no_punc.append(w.lower())

        fdist2 = FreqDist(words_no_punc)

        stopwords_ = stopwords.words("english")

        clean_words = []

        for w in words_no_punc:
            if w not in stopwords_:
                clean_words.append(w)

        fdist3 = FreqDist(clean_words)

        most_common = pd.DataFrame(fdist3.most_common(10))
        df = pd.DataFrame({"words": most_common[0], "count": most_common[1]})
        fig = px.line(df, x="words", y="count", title='')
        st.plotly_chart(fig)

        wordcloud = WordCloud().generate(str1)
        st.subheader("III - Wordcloud")
        agree = st.checkbox("Click here to generate wordcloud.")
        if agree:
            st.image(wordcloud.to_array())


st.header("Part B - Most Popular Articles")

st.write("Select if you want to see the most shared, emailed or viewed articles.")
option2 = st.selectbox("Select your preferred set of articles.",
                       ["", "Shared", "Emailed", "Viewed"])

option3 = st.selectbox("Select the period of time (last days).",
                       ["", "1", "7", "30"])

base_url = "https://api.nytimes.com/svc/mostpopular/v2/"

if option2 and option3:
    wordcloud_two = WordCloud().generate(str1)
    st.image(wordcloud_two.to_array())
