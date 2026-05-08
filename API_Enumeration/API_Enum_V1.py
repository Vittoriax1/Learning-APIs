import requests

# change this to your test API
base_url = "http://localhost:8000"  
# Feel free to add additional words
wordlist = [
    "api",
    "auth",
    "users",
    "status",
    "login",
    "health",
    "v1",
    "v2",
    "admin"
    "doc"
    "docs"
]

print("Enumerating endpoints...\n")

for path in wordlist:
    url = f"{base_url}/{path}"
    try:
        response = requests.get(url, timeout=3)
        print(f"{url} -> {response.status_code}")
    except Exception as e:
        print(f"{url} -> error")

print("Enumeration complete.")
