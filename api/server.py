from dotenv import load_dotenv
import os
from fastapi import FastAPI, FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import boto3
import hashlib

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

    # Get file contents
    file_bytes = file.file.read()

    # Hash the filename 
    file_hash = hashlib.md5(file.filename.encode())
    file_hash_str = file_hash.hexdigest()
    
    # Upload to S3
    s3_client.put_object(
        Bucket="image-upload-main",
        Key=file_hash_str,
        Body=file_bytes,
        ACL="public-read"
    )
    
    object_url = f"https://image-upload-main.s3.amazonaws.com/{file_hash_str}"

    return JSONResponse({
        "success": status,
        "url": object_url
    })

@app.delete("/image/{image_id}")
async def delete_image():
    return {""}