# Installing LM Studio
https://lmstudio.ai/

# Installing Tesseract
https://github.com/tesseract-ocr/tesseract

# Installing dependencies
Run this in the command line
```
pip install -r requirements.txt
```
# Setting up LM Studio
1. In Home, find the Llama 3.1 8B Instruct Model
2. Choose and download a quantized model (Q4 and above is recommended)
3. Go to Local Server -> Select model to load

# CORS configuration
In main.py make sure the URL you are sending request from is included in the origins array

You can now call /receipt/post to get your receipt's information
