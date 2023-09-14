# azureml-core of version 1.0.72 or higher is required
from azureml.core import Workspace, Run
from azureml.core.authentication import ServicePrincipalAuthentication

import tensorflow
from tensorflow import keras
import numpy as np
import io
import os
from PIL import Image   
from tensorflow.keras.layers import Input, Dense, Dropout, Flatten, BatchNormalization

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response, FileResponse
import uvicorn

from skimage import data, color, filters, morphology,transform, exposure, feature, util
from matplotlib.image import imread

cwd = os.getcwd()
print("current", cwd)

#env variables ophaelen van azure 
subscription_id = os.environ.get("subscription_id")
resource_group = os.environ.get("resource_group")
workspace_name = os.environ.get("workspace_name")
workspace_id = os.environ.get("workspace_id")

svc_pr_password = os.environ.get("svc_pr_password")

#Authenticatie
svc_pr = ServicePrincipalAuthentication(
    tenant_id=os.environ.get("tenant_id"),
    service_principal_id=os.environ.get("service_principal_id"),
    service_principal_password=svc_pr_password)

ws = Workspace(subscription_id, resource_group, workspace_name,auth=svc_pr)

aml_context = Run.get(ws,workspace_id)
print('starting model download')
#Model ophalen uit de azure ml
aml_context.download_file('outputs/model.h5', output_file_path='download/', _validate_checksum=False)

print("tot hier")

model = keras.models.load_model("download/model.h5")

print("na model inlezen")
print(model)

#FASTAPI
app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello World"}


@app.post("/predict/test")
async def predict_api(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    
    prediction = predict(image)
    return prediction

def predict(im: Image.Image):
    #image = Image.open(im)
    image_size = 100
    #im = imread(im)
    #im = transform.resize(im,(image_size,image_size),mode='constant',anti_aliasing=True)
    image = im.resize((100, 100))
    image = np.asarray(image)
    #image_array = np.array(image)
    print(image.shape)

    image = np.reshape(image, (1, 100, 100, 3))  

    result = model.predict(image)   

    #PIL_image = Image.fromarray(result.astype('uint8'), 'RGB')
    from tensorflow.keras.preprocessing.image import array_to_img
    result = np.reshape(result, (100, 100, 3))  
    PIL_image = array_to_img(result)
    PIL_image.save('result.jpg')
    print(result)
    return FileResponse('result.jpg') #Response(content=result.jpg, media_type="image/jpg")
    
def read_imagefile(file) -> Image.Image:
    image = Image.open(io.BytesIO(file))
    return image

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8800)