import random
import task_repository

def generate_id() -> int:
    task_id = None
    while True:
        task_id = random.randint(1, 1_000_000)

        if not task_repository.exists_by_id(task_id):
            break

    return task_id

def generate_status(finished_date: str) -> str:
    return "In Progress" if finished_date is None else "Finished"
