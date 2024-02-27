import uvicorn
from fastapi import FastAPI,File,UploadFile
from io import BytesIO
import numpy as np
from PIL import Image
import tensorflow as tf
import requests

app = FastAPI()

endpoints = "http://localhost:8501/v1/models/potato_model:predict"
CLASS_NAMES =['Early Blight','Late Blight','Healthy']

@app.get('/ping')
async def root():
   return {"message": "Hello World"}

def read_file_as_image(data) -> np.ndarray:
   image = np.array(Image.open(BytesIO(data)))
   return image

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
   image = read_file_as_image(await file.read())
   img_batch = np.expand_dims(image,0)
   json_data = {

      "instances":img_batch.tolist()
   }
   response = requests.post(endpoints,json=json_data)
   prediction = np.array(response.json()["predictions"][0])
   predicted_class = CLASS_NAMES[np.argmax(prediction)]
   confidence = np.max(prediction)
   pass
   return {
        "class": predicted_class,
        "confidence": float(confidence)
    }                                                                                                                                                                                                                                                                                                  
   
if __name__ == "__main__":
   uvicorn.run("tf_serving:app", host="localhost", port=4444)