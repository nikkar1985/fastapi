!pip install fastapi uvicorn





%%writefile main_v4.py
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def init_db():
    conn = sqlite3.connect("my_workspace.db")
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS tasks ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

class TaskInput(BaseModel):
    title: str
    priority: int

@app.post("/add-task")
def add_task(task: TaskInput):
    conn = sqlite3.connect("my_workspace.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", (task.title, task.priority))
    conn.commit()
    conn.close()
    return {"status": "Οκ αποθηκεύτηκε στη βάση"}

@app.get("/show-tasks")
def show_tasks():
    conn = sqlite3.connect("my_workspace.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, priority FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    
    tasks_list = [{"id": r[0], "title": r[1], "priority": r[2]} for r in rows]
    return {"database_content": tasks_list}





!fuser -k 8000/tcp
get_ipython().system_raw('uvicorn main_v3:app --host 127.0.0.1 --port 8000 &')
print("Ο server δουλεύει κανονικά στην θύρα 8000")






import requests
import time

time.sleep(2)

res_empty = requests.get("http://127.0.0.1:8000/show-tasks")
print("Αρχική βάση:", res_empty.json())


requests.post("http://127.0.0.1:8000/add-task", json = {"title": "Μαθαίνω Python", "priority":1})



res_full = requests.get("http://127.0.0.1:8000/show-tasks")
print("Περιεχόμενο της βάσης: ", res_full.json())
