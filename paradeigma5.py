!pip install fastapi uvicorn




%%writefile main_v3.py
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Task(BaseModel):
  title: str
  priority: int
  completed:bool = False

@app.post("/create-task")
def create_task(task: Task):
  return {"status": "Επιτυχία",
          "μήνυμα" : f"Η εργασία '{task.title}' δημιουργήθηκε με προτεραιότητα {task.priority}.",
          "δεδομένα_που_λάβαμε": task}







!fuser -k 8000/tcp
get_ipython().system_raw('uvicorn main_v3:app --host 127.0.0.1 --port 8000 &')
print("Ο server δουλεύει κανονικά στην θύρα 8000")








import requests
import time

time.sleep(2)

payload_correct = {"title" : "Διάβασμα για την γλώσσα python",
                   "priority": 1,
                   "completed": False}

res1= requests.post("http://127.0.0.1:8000/create-task", json=payload_correct)
print("Check για σωστό αίτημα")
print("Status Code:", res1.status_code)
print("Απάντηση :", res1.json() )
