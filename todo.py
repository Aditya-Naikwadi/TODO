import json
import os

# Configuration
FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Save the task list to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n" + "="*25)
    print("   TO-DO LIST PRO")
    print("="*25)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Done")
    print("4. Remove Task")
    print("5. Exit")
    print("="*25)

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == '1':
            print("\n--- YOUR TASKS ---")
            if not tasks:
                print("Your list is currently empty.")
            else:
                for i, t in enumerate(tasks, 1):
                    status = "[✔]" if t['done'] else "[ ]"
                    print(f"{i}. {status} {t['task']}")

        elif choice == '2':
            task_name = input("Enter the task name: ").strip()
            if task_name:
                tasks.append({"task": task_name, "done": False})
                save_tasks(tasks)
                print(f"Task '{task_name}' added!")

        elif choice == '3':
            # View tasks first so user knows the index
            if not tasks:
                print("Nothing to mark as done.")
                continue
            
            try:
                idx = int(input("Enter task number to toggle status: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks[idx]['done'] = not tasks[idx]['done']
                    save_tasks(tasks)
                    print(f"Updated status for: {tasks[idx]['task']}")
                else:
                    print("Error: Invalid task number.")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '4':
            if not tasks:
                print("Nothing to remove.")
                continue
            
            try:
                idx = int(input("Enter task number to remove: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['task']}")
                else:
                    print("Error: Invalid number.")
            except ValueError:
                print("Error: Please enter a numeric value.")

        elif choice == '5':
            print("Progress saved. Goodbye!")
            break

        else:
            print("Invalid input. Please choose 1-5.")

if __name__ == "__main__":
    main()