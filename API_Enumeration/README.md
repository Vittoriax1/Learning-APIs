# API_Enum_V1
API_Enum_V1.py is a simple, beginner‑friendly Python script designed to help you enumerate API endpoints in a development or test environment.
This tool is useful for:
- Learning how APIs are structured
- Mapping available routes in your own lab environments
- CTFs where enumeration is explicitly allowed
- Understanding how automated recon works in a safe, ethical way

## How It Works
The script sends harmless GET requests to a list of common API paths and logs which ones respond.
It will:
- Build full URLs based on a base address
- Try each path in the wordlist
- Report HTTP status codes
- Handle errors cleanly

This helps reveal which endpoints exist in your API surface — in environments where you have permission to test.

## Requirements
To run this script, you need:

Python 3.8+
requests library

Install dependencies:
pip install requests


## Usage

Open the script and set your target base URL:

base_url = "http://localhost:8000"
Adjust the base_url to that target if it is different than what is coded within the script.

Adjust the wordlist in the script if desired.
Run the script:

python3 API_Enum_V1.py

You will see output like:
http://localhost:5000/api -> 200
http://localhost:5000/status -> 404
http://localhost:5000/users -> 403

## Intended Use
This script is for authorized testing only.
It is designed for use in:
- Your own local development APIs
- Lab machines
- Capture‑The‑Flag (CTF) events that explicitly allow API probing
- Educational environments

Never run this script against systems you do not have permission to test.
