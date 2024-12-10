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

If you are testing with a physical device, connect your computer to your phone's hotspot

Run this on the command line get ip4 address
```
ipconfig
```
Run the server with this command
```
uvicorn main:app --reload --host <your ip4>  --port 8000
```

You can now call the endpoint to get your receipt's information
```
http://<your ip4>:8000/receipt/post
```
