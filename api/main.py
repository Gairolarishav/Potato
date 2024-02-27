import uvicorn
from fastapi import FastAPI,File,UploadFile
from io import BytesIO
import numpy as np
from PIL import Image
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model("/home/rshavgairola/Documents/Projects/Potato/saved_models/1")
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
   predictions = MODEL.predict(img_batch)
   predict_class = CLASS_NAMES[np.argmax(predictions[0])]  
   confidence = np.max(predictions[0]) 
   print(predict_class,confidence) 
   return { 'class' : predict_class,'confidence' :float(confidence)}                                                                                                                                                                                                                                                                                                      
   
if __name__ == "__main__":
   uvicorn.run("main:app", host="localhost", port=4000, reload=True)