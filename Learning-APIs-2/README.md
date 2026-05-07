# Learning APIs 2

This project expands on the basic FastAPI example by adding simple API key authentication.

The /hello endpoint now requires a valid x-api-key header before it will return a response.

## Setup
Install the required packages:

pip install fastapi uvicorn

Make sure your script is named main.py and is in the project directory.

## Running the API

Start the FastAPI server using Uvicorn:

uvicorn main:app --reload

- main → your Python file name (without .py)
- app → the FastAPI instance inside the file
- --reload → enables automatic reloading when you make edits
## Authentication

This API uses a simple static API key:

mysecretkey123

You must include the header x-api-key in your request.

### Example request (correct key)
curl -H "x-api-key: mysecretkey123" 
http://127.0.0.1:8000/hello

Response:
{"message": "Hello, authorized user!"}

### Example request (incorrect or missing key)
curl -H "x-api-key: wrongkey" 
http://127.0.0.1:8000/hello

Response:
{"detail":"Invalid or missing API key"}

## Interactive API Docs
FastAPI automatically generates live documentation:

#### Swagger UI:
http://127.0.0.1:8000/docs

#### ReDoc:
http://127.0.0.1:8000/redoc

## File Structure
Learning-APIs-2/

├── main.py

└── README.md
