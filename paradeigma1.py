!pip install fastapi uvicorn


%%writefile main.py
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello World το API δουλεύει"}




get_ipython().system_raw('uvicorn main:app --host 127.0.0.1 --port 8000 &')
print("Ο server δουλεύει κανονικά στην θύρα 8000")



import requests
import time

time.sleep(2)
response = requests.get("http://127.0.0.1:8000/")
print("Status Code:", response.status_code)
print("Απάντηση από το API: ", response.json())





