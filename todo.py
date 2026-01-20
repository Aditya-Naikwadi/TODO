import sys

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("Your list is empty.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print("Task added successfully!")

        elif choice == '3':
            if not tasks:
                print("Nothing to remove.")
                continue
            
            # Show tasks so user knows what number to pick
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
                
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()