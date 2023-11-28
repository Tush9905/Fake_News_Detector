import streamlit as st
from transformers import pipeline
import requests
from huggingface_token import token

st.write("# Fake News Detector")
API_URL = "https://api-inference.huggingface.co/models/tush9905/fake_news_detector"
headers = {"Authorization": f"Bearer {token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

with st.form("my_form"):
    news_article = st.text_input(label="Copy and Paste the News Article Here.")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        Result = query({"inputs": news_article})
        Label = Result[0][0]["label"]
        Score = Result[0][0]["score"]
        Label_not = Result[0][1]["label"]
        Score_not = Result[0][1]["score"]
        if Label == "RELIABLE":
            st.success(f"Looks {int(Score*100)}% {Label}")
        else:
            st.error(f"Looks {int(Score*100)}% {Label}")

        st.write(f"{Label} : {Score*100}%")
        st.write(f"{Label_not} : {Score_not*100}%")
        



