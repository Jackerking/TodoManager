import os

TASKS_FILE = "tasks.txt"

def add_task(task):
    with open(TASKS_FILE, "a") as f:
        f.write(f"{task}\n")

def list_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return f.read().splitlines()
