import json

import services
from task import Task

def get_taskjson():
    try:
        with open('tasks.json', 'r') as tasks:
            return json.load(tasks)
    except FileNotFoundError:
        print("Error: File Not Found.")

tasks_json: list = get_taskjson()

def add_task(task: Task) -> bool:
    global tasks_json

    the_task = {
        "ID":task.task_id,
        "Task": task.task,
        "Date added":str(task.date_added),
        "Date finished":"Not yet finished.",
        "Status":services.generate_status(None)
    }

    try:
        with open('tasks.json', 'w') as tasks:
            tasks_json.append(the_task)
            
            json.dump(tasks_json, tasks, indent=4)
            return True
    except FileNotFoundError:
        print("Error: File Not Found.")

    return False

def exists_by_id(id: int) -> bool:
    for task in get_taskjson():
        if task["ID"] == id:
            return True
    
    return False

def get_taskbyid(id: int) -> Task | None:
    global tasks_json

    for task in tasks_json:
        if id == task["ID"]:
            return Task(task["ID"], task["Task"], task["Date added"], task["Date finished"])
    
    return None

def mark_finished(task: Task) -> bool:
    global tasks_json

    task_as_finished = {
        "ID":task.task_id,
        "Task":task.task,
        "Date added":str(task.date_added),
        "Date finished":str(task.date_finished),
        "Status":services.generate_status(task.date_finished)
    }

    for i in range(len(tasks_json)):
        if tasks_json[i]["ID"] == task.task_id:
            tasks_json.remove(tasks_json[i])
            tasks_json.insert(i, task_as_finished)
            break

    try:
        with open('tasks.json', 'w') as tasks:
            json.dump(tasks_json, tasks, indent=4)

            return True
    except FileNotFoundError:
        print("File Not Found.")
    
    return False

def mark_unfinished(task: Task) -> bool:
    global tasks_json

    task_as_finished = {
        "ID":task.task_id,
        "Task":task.task,
        "Date added":str(task.date_added),
        "Date finished":"Not yet finished.",
        "Status":services.generate_status(None)
    }

    for i in range(len(tasks_json)):
        if tasks_json[i]["ID"] == task.task_id:
            tasks_json.remove(tasks_json[i])
            tasks_json.insert(i, task_as_finished)
            break

    try:
        with open('tasks.json', 'w') as tasks:
            json.dump(tasks_json, tasks, indent=4)

            return True
    except FileNotFoundError:
        print("File Not Found.")
    
    return False

def delete(task_todel: Task) -> bool:
    global tasks_json

    for task in tasks_json:
        if task["ID"] == task_todel.task_id:
            tasks_json.remove(task)
            break

    try:
        with open('tasks.json', 'w') as tasks:
            json.dump(tasks_json, tasks, indent=4)

            return True
    except FileNotFoundError:
        print("File Not Found.")
    
    return False