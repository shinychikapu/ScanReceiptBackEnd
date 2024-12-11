# Installing Python
https://docs.python.org/3/using/windows.html

https://docs.python.org/3/using/mac.html

https://docs.python.org/3/using/unix.html

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

You should be able to test the receipt scanning features after following these steps. Note that an Android phone is required to test with the front end. If you don't have an android phone to follow **Testing without the Front End**

## Testing without the Front End
1. Run the server
   ```
   uvicorn main:app --reload
   ```
2. By default the back end will run at 127.0.0.1:8000. Go to this page in your browser
   ```
   http://127.0.0.1:8000/docs
   ```
3. Click on this bar
   ![image](https://github.com/user-attachments/assets/35c58619-0e2b-4cfb-952f-48c60e4d9c25)
4. Click on try it out
   ![image](https://github.com/user-attachments/assets/0a1bd954-8c93-47cd-a35a-c243f4d6c74e)
5. Choose a file which is an image of a receipt and click Execute
   ![image](https://github.com/user-attachments/assets/ba29db31-7320-4d85-b8ab-91d18fb3ff34)
6. If the receipt is scanned successfully it will return code 200 like the image below. Otherwise it return code 400 and you might want to try with another photo
   ![image](https://github.com/user-attachments/assets/a4a49d2a-f889-40f6-a221-0fb8dbb97005)

    

