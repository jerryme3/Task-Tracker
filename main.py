import sys
import services
from datetime import date

import task_repository
from task import Task

def main(cli_task: str, action=''):
    
    match cli_task:
        case 'help':
            print("===========================================ALL COMMANDS======================================")
            print("1. add      - lets you add a task to the json file. Format: python main.py add \"task\"")
            print("2. mark-fin - lets you mark a task as finished. Format: python main.py mark-fin \"task-id\"")
            print("3. mark-uf  - lets you mark a task as unfinished. Format: python main.py mark-unf \"task-id\"")
            print("4. see-all  - lets you see all of your listed tasks. Format: python main.py see-all")
            print("5. see-fin  - lets you see all of you finished tasks. Format: python main.py see-fin")
            print("6. see-uf   - lets you see all of your unfinished tasks. Format: python main.py see-uf")
            print("7. del      - lets you delete a specific task within your list. Format: python main.py del \"task-id\"")
        case 'add':
            if str(action).isspace() or len(action) == 0:
                print("Task to be added is expected, but none was passed.")
                return
            
            print("TASK ADDED SUCCESSFULLY!" if task_repository.add_task(Task(services.generate_id(), action, date.today(), None)) else "UNEXPECTED ERROR OCCURRED.")
        case 'mark-fin':
            if str(action).isspace() or len(action) == 0:
                print("Task ID to be marked as finished is expected, but none was passed.")
                return
            
            if not str(action).isdigit():
                print("Input must only contains numerical characters.")
                return

            task = task_repository.get_taskbyid(int(action))
            
            if task is None:
                print("Task ID does not exists.")
                return
            
            if task.date_finished != "Not yet finished.":
                print("This task is already finished.")
                return
            
            task.date_finished = date.today()

            print("MARKED AS FINISHED SUCCESSFULLY!" if task_repository.mark_finished(task) else "UNEXPECTED ERROR OCCURRED.")
        case 'mark-uf':
            if str(action).isspace() or len(action) == 0:
                print("Task ID to be marked as unfinished is expected, but none was passed.")
                return
            
            if not str(action).isdigit():
                print("Input must only contains numerical characters.")
                return
            
            task = task_repository.get_taskbyid(int(action))

            if task is None:
                print("Task ID does not exists.")
                return
            
            if task.date_finished == "Not yet finished.":
                print("This task is unfinished. No need to mark as one.")
                return

            print("MARKED AS UNFINISHED SUCCESSFULLY!" if task_repository.mark_unfinished(task) else "UNEXPECTED ERROR OCCURRED.")

        case 'see-all':
            inc = 0
            tasks = task_repository.tasks_json

            if len(tasks) == 0:
                print("You haven't added any tasks yet. Add now!")
            
            for task in tasks:
                inc+=1
                print(f"{inc}. Task ID: {task["ID"]} | Task: {task["Task"]} | Date added: {task["Date added"]} | Date finished: {task["Date finished"]} | Status: {task["Status"]}")

        case 'see-fin':
            inc = 0
            tasks = task_repository.tasks_json

            if len(tasks) == 0:
                print("You haven't added any tasks yet. Add now!")
            
            for task in tasks:
                if task["Date finished"] != "Not yet finished.":
                    inc+=1

                    print(f"{inc}. Task ID: {task["ID"]} | Task: {task["Task"]} | Date added: {task["Date added"]} | Date finished: {task["Date finished"]} | Status: {task["Status"]}")

        case 'see-uf':
            inc = 0
            tasks = task_repository.tasks_json

            if len(tasks) == 0:
                print("You haven't added any tasks yet. Add now!")
            
            for task in tasks:
                inc+=1

                if task["Date finished"] == "Not yet finished.":
                    print(f"{inc}. Task ID: {task["ID"]} | Task: {task["Task"]} | Date added: {task["Date added"]} | Date finished: {task["Date finished"]} | Status: {task["Status"]}")
        
        case 'del':
            if str(action).isspace() or len(action) == 0:
                print("Task ID to be marked as unfinished is expected, but none was passed.")
                return
            
            if not str(action).isdigit():
                print("Input must only contains numerical characters.")
                return
            
            task = task_repository.get_taskbyid(int(action))

            if task is None:
                print("Task ID does not exists.")
                return
            
            print("TASK DELETED SUCCESSFULLY." if task_repository.delete(task) else "AN UNEXPECTED ERROR OCCURRED.")

if __name__ == '__main__':

    if (len(sys.argv) < 2):
        print("Actions are expected, but none was passed.")
        sys.exit(0)

    if sys.argv[1] != 'help':
        print("To see all of the commands, enter \"python main.py help\"")

    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '')
