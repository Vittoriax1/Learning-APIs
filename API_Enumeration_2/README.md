# API_Enum_V2
API_Enum_V2.py is an enhanced API endpoint enumeration tool designed for learning, development, labs, and CTF environments where enumeration is explicitly allowed.

This script improves on Version 1 by adding:
- Reading a wordlist from a file
- Testing nested paths (example: api/v1/users)
- Logging results to a file
- Threading for faster enumeration
- Reporting response size and content type

It remains safe for authorized testing only.

## Features

1. Reads a wordlist from a file
Place your path names inside wordlist.txt.
Each line represents one endpoint to test.
2. Supports nested prefixes
The script can automatically test patterns like:

- /api/x
- /api/v1/x
- /v1/x
- /v2/x
- <i>Feel free to add other options as needed.</i>

3. Logs results to a file
Output is saved to enum_results.txt for later review.
4. Multithreaded for speed
Uses multiple worker threads to enumerate endpoints faster.
5. Shows response size and content type
Example output:
http://localhost:5000/api/users -> 200 | size=452 bytes | type=application/json



## Requirements
Install Python dependencies:
pip install requests


## Usage

Set your target URL inside the script:

BASE_URL = "http://localhost:5000"



Add your endpoints to wordlist.txt.


Run:


python3 API_Enum_V2.py



The output shows the test results.

Example:

http://localhost:5000/api -> 200 | size=93 bytes | type=application/json

http://localhost:5000/users -> 404 | size=12 bytes | type=text/html


Review saved results in:

enum_results.txt


## Intended Use
This script is for authorized testing only, including:

Local development environments
Personal lab machines
CTFs where scanning/enumeration is explicitly allowed

Never run this tool against systems you do not own or have permission to test.

## File Structure
/API_Enum_V2/
│
├── API_Enum_V2.py
├── wordlist.txt
└── enum_results.txt   (created automatically)

