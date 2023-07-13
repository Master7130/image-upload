from fastapi import FastAPI
import boto3

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/image/{image_id}")
async def get_image():
    return {""}

@app.post("/image")
async def upload_image():
    return {""}

@app.delete("/image/{image_id}")
async def delete_image():
    return {""}