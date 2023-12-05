# Fake News Detector
* Achieved **99.55%** Accuracy in Fake News Detection using Natural Language Processing (NLP) by Fine Tuning the **BERT LLM Transformer** on a Dataset of 72,133 News Articles using Python, Pandas, PyTorch, Hugging Face.
* Used **Hugging Face Hub** with **Hugging Face Inference API** for **MLOps / Deploying** the Model.
* Developed an Interactive Web App using Streamlit.
* Tech Used - **Python, Pandas, PyTorch, Hugging Face, Streamlit.**

## How to use it in your projects (2 Ways) -
### Using API Calls with Hugging Face Inference API (Recommended for using it directly in your App)
``` python
import requests
from huggingface_token import token
# Use your own token

st.write("# Fake News Detector")
API_URL = "https://api-inference.huggingface.co/models/tush9905/fake_news_detector"
headers = {"Authorization": f"Bearer {token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
```
### OR
### By Importing the Model Itself
  ``` python
  from transformers import AutoModel
  model = AutoModel.from_pretrained("tush9905/fake_news_detector")
  ```
