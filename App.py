import streamlit as st
import os
from dotenv import load_dotenv
import requests

st.title("Fake News Detector")

load_dotenv()
huggingface_token = os.environ["HUGGINGFACE_HUB_TOKEN"]
API_URL = "https://api-inference.huggingface.co/models/tush9905/fake_news_detector"
headers = {"Authorization": f"Bearer {huggingface_token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

with st.form("my_form"):
   email = st.text_input("Copy and Paste the News Article")
   submit = st.form_submit_button('Check')

   if submit:
      model_output = query({"inputs": email})
      label = model_output[0][0]["label"]
      score = model_output[0][0]["score"]
      label_not = model_output[0][1]["label"]
      score_not = model_output[0][1]["score"]
      if label == "UNRELIABLE":
        st.error(f"The News looks {int(score*100)}% {label}")
        st.write()
      else:
         st.success(f"The News looks {int(score*100)}% {label}")

      st.write(f"{label} : {score*100}%")
      st.write(f"{label_not} : {score_not*100}")