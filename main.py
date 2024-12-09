from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os, re
from receipt_ocr import getReceiptJSON
 
 #uvicorn main:app --reload

from pydantic import BaseModel
class Receipt(BaseModel):
    category: str
    date: str
    total: float

app = FastAPI()

# CORS configuration
origins = [
    "http://10.3.0.86",  # Your development machine's IP
    "http://10.3.0.25",
    "http://localhost",
    "http://127.0.0.1",
    "http://192.168.87.228",
    "*",  # Allow all origins for testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/receipt/post")
async def getReceiptInfo(file: UploadFile = File(...)):
    """
    Endpoint to process uploaded receipt image and return extracted information.
    
    Args:
        file (UploadFile): Image file uploaded by the user.

    Returns:
        JSON response with receipt details.
    """
    try:
        sanitized_filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', file.filename)
        print(f"Sanitized file name: {sanitized_filename}")
        # Save uploaded file to disk
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, sanitized_filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Process the receipt image
        result = getReceiptJSON(file_path)

        # Validate result with the Receipt model
        receipt = Receipt(**result)
        return receipt.model_dump_json()

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing receipt: {e}")
