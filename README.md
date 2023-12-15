# Fake News Detector
* Achieved **99.55%** Accuracy in Fake News Detection using Natural Language Processing (NLP) by Fine Tuning the **BERT LLM Transformer** on a Dataset of 72,133 News Articles using Python, Pandas, PyTorch, Hugging Face.
* Used **Hugging Face Hub** with **Hugging Face Inference API** for **MLOps / Deploying** the Model.
* Developed an Interactive Web App using Streamlit.
* Tech Used - **Python, Pandas, PyTorch, Hugging Face, Streamlit.**

## How to use it in your projects (2 Ways) -
### Using API Calls with Hugging Face Inference API (Recommended for using it directly in your App)
``` python
import streamlit as st
import os
from dotenv import load_dotenv
import requests

load_dotenv()
huggingface_token = os.environ["HUGGINGFACE_HUB_TOKEN"]
API_URL = "https://api-inference.huggingface.co/models/tush9905/fake_news_detector"
headers = {"Authorization": f"Bearer {huggingface_token}"}
```
### OR
### By Importing the Model Itself
  ``` python
  from transformers import AutoModel
  model = AutoModel.from_pretrained("tush9905/fake_news_detector")
  ```
