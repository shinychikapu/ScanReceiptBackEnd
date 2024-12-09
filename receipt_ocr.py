from openai import OpenAI
import json
from PIL import Image
import numpy as np
import cv2
import pytesseract
import jsonschema

schema = {
    "type": "object",
    "properties": {
        "category": {"type": "string"},
        "date": {"type": "string"},
        "total": {"type": "number"}
    },
    "required": ["category", "total"]
  }
def correct_image_orientation(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Check if the image has EXIF data (metadata)
    try:
        # Extract EXIF data
        exif = img._getexif()
        if exif is not None:
            # Find the orientation tag
            for tag, value in exif.items():
                if tag == 274:  # Orientation tag in EXIF
                    # Rotate the image based on the orientation value
                    if value == 3:
                        img = img.rotate(180, expand=True)
                    elif value == 6:
                        img = img.rotate(270, expand=True)
                    elif value == 8:
                        img = img.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # If no EXIF data exists, skip the correction
        pass
    return img

def preprocess_image(image_path):
    dpi = 300
    img = correct_image_orientation(image_path)
    img.info['dpi'] = (dpi, dpi)
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #opt_thr, img_ = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    return gray

def get_text(image_path):
    text = pytesseract.image_to_string(preprocess_image(image_path), config = f'--oem 1 --psm 3')
    print("Extracted text:")
    print(text)
    return text

def extract_receipt(image, inference_url = "http://localhost:1234/v1"):
    client = OpenAI(base_url=inference_url, api_key="lm-studio")
    system_prompt = """You are a helpful assistant trained to extract structured information from unstructured text. Your task is to process scanned receipt text and output JSON object with three require pieces of information.

The model you are generating should have three fields:
1. **category**: The spending category which belongs to food, shopping, grocery, medical and misca
2. **date**: The date the receipt was issued in the format "MM/DD/YYYY".
3. **total**: The total amount spent, formatted as a number (e.g., "25", "123.45").

### Instructions:
- Identify the spending category, date, and total amount. 
- If any information is missing, leave the corresponding field blank.
- Ensure the output strictly adheres to the following JSON Schema:
  schema = {
    "type": "object",
    "properties": {
        "category": {"type": "string"},
        "date": {"type": "string"},
        "total": {"type": "number"}
    },
    "required": ["category", "amount"]
  }
- Output only the JSON Schema as the example showed
- DO NOT INCLUDE ANY COMMENTATION OR CONVERSATION
- DO NOT INCLUDE "Here is the extracted information in JSON format:..." in output

### Example:
- Input:
Boiling Point
123 Alexander Ave, San Jose, CA 95112
01/12/2024
1. Seafood Hot Pot              $15.99
2. Beef Hot Pot                 $17.99
Subtotal                        $33.98
Tax                             $3.4
Total                           $37.38

- Output:
{
  "category": "Food",
  "date": "01/12/2024",
  "Total": 37.38
}
"""
    user_prompt = '''Below is the receipt that you need to extract information from.
{}'''
    text = get_text(image)
    response = client.beta.chat.completions.parse(
    model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt.format(text)}
    ],
    max_tokens = 50,
    temperature= 0.1,
    response_format= schema
    )
    #convert to lower case to avoid random capitalization
    result = json.loads(response.choices[0].message.content.lower()) 
    print(json.dumps(result , indent=2))
    return result

def getReceiptJSON(image_path):
    try:
        receipt_json = extract_receipt(image_path)
        # Validate JSON against the schema
        jsonschema.validate(instance=receipt_json, schema=schema)
        print("Data is valid!")
        return receipt_json
    except Exception as e:
        print(f"Error processing receipt: {e}")
        return {}

# Example usage (can be removed in deployment)
if __name__ == "__main__":
    test_image_path = r"uploads\2c649abc-2437-4655-9acf-c925aefa37822787772395577112386.jpg"
    result = getReceiptJSON(test_image_path)
    print(json.dumps(result, indent=4))
