from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "mysecretkey123"

@app.get("/hello")
def hello(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    return {"message": "Hello, authorized user!"}
