# Learning APIs 1
This repository contains a simple FastAPI application created as part of learning how APIs work. It exposes a single GET endpoint at /hello and demonstrates the basics of building and running an API with Python.

## Setup
Make sure you have Python 3.8+ installed.

Install the required packages:

pip install fastapi uvicorn

## Running the API
Start the server with Uvicorn:

uvicorn main:app --reload
- main is the name of the Python file (without the .py)
- app is the FastAPI app instance created in the file
--reload enables auto-reload when files change

## Using the API
Once running, open this in the browser:

http://127.0.0.1:8000/help

## Interactive Docs
FastAPI includes automatic documentation:

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc
