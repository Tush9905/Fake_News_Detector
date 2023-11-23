import streamlit as st
from transformers import pipeline

st.write("# Fake News Detector")
classifier = pipeline("text-classification", model="./fake_news_detector/")

with st.form("my_form"):
    news_article = st.text_input(label="Copy and Paste the News Article Here.")
    submitted = st.form_submit_button("Submit")
    if submitted:
        Result = classifier(news_article)
        Label = Result[0]["label"]
        Score = Result[0]["score"]
        if Label == "RELIABLE":
            st.success(f"Looks {int(Score*100)}% {Label}")
        else:
            st.error(f"Looks {int(Score*100)}% {Label}")



