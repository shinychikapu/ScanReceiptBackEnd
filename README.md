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

## Testing with a physical device (For Android Phones)

For this you need to connect your computer to your phone's hotspot

Run this on the command line get ip4 address
```
ipconfig
```
## Running the back end server
First activate the virtual environment 
```
venv\Scripts\activate
```
Run the server with this command
```
uvicorn main:app --reload --host <your ip4>  --port 8000
```

In the front end repo, go to camera_page.dart. In the **_sendImageToBackend()** function. On line 41 change the value of the url to fit with your ip4 address
```
final url = Uri.parse('http:<your ip4>:8000/receipt/post');
```
## Example of test with an Android phone

Start your local server in LM Studio before following these steps. Also connect your computer to your phone's hotspot

1. Get IPv4 Address
![image](https://github.com/user-attachments/assets/7fc7aa5e-fa8d-428d-ae41-e53a0b795251)

2. Activate the virtual Environment
![image](https://github.com/user-attachments/assets/f78e097c-7648-4718-8c94-2b4d081a989f)

3. Run the server
![image](https://github.com/user-attachments/assets/7a21d956-d795-4af1-85d5-c7e0d34ffd72)

4. Modify the front end code
![image](https://github.com/user-attachments/assets/8782abf4-83ea-44ac-9060-471a3ba6a3d1)

You should be able to test the receipt scanning features after following these steps
