import sys
from utils import add_task, list_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        task = sys.argv[2]
        add_task(task)
        print(f'Task "{task}" added.')
    elif command == "list":
        tasks = list_tasks()
        print("Todo List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
