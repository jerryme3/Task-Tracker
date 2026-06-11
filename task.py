from datetime import date

class Task:

    def __init__(self, task_id: int, task: str, date_added: date, date_finished: date):
        self.task_id       = task_id
        self.task          = task
        self.date_added    = date_added
        self.date_finished = date_finished