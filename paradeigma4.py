!pip install fastapi uvicorn



%%writefile main_v2.py
from fastapi import FastAPI

app= FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
  return {"message": f"Θα εκτυπωθεί το ID : {item_id}"}

@app.get("/greet")
def greet_user(username: str = "Επισκέπτης"):
  return {"message": f"Καλως ήρθατε {username}"}




!fuser -k 8000/tcp
get_ipython().system_raw('uvicorn main_v2:app --host 127.0.0.1 --port 8000 &')
print("Ο server δουλεύει κανονικά στην θύρα 8000")




import requests
import time

time.sleep(2)
res1 = requests.get("http://127.0.0.1:8000/items/105")

print("Απάντηση 1: ", res1.json())


res2= requests.get("http://127.0.0.1:8000/greet?username=Nik")
print("Απάντηση 2 : ", res2.json())


res3= requests.get("http://127.0.0.1:8000/greet")
print("Απάντηση 3: ", res3.json())

