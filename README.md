# Fake_News_Predictor
* Achieved **99.86%** Accuracy in Fake News Detection using Natural Language Processing (NLP) by Fine Tuning the **DeBERTa LLM Transformer** on a Dataset of 72,133 News Articles using Python, Pandas, PyTorch, Hugging Face.
* It is not Overfit

## How to use it in your projects -

### ***Note - Since the actual model size exceeds the Github and Github LFS Free Limit, the model files aren't included. However, you can generate the model by running the Model_Notebook.ipynb.***
  
* You can use hugging face pipeline and import the model using the config in the generated folder -

  ``` python
  from transformers import pipeline
  classifier = pipeline("text-classification", model="./fake_news_detector/")
  ```
