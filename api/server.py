from dotenv import load_dotenv
import os
from fastapi import FastAPI, FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import boto3

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initializing boto3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/image/{image_id}")
async def get_image():
    return {""}

@app.post("/image")
async def upload_image(file: UploadFile = File(...)):
    status = True

    return JSONResponse({
        "success": status,
        "url": "url"
    })

@app.delete("/image/{image_id}")
async def delete_image():
    return {""}