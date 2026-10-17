from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)


def main():
    tasks = []
    while True:
        print("\n--- Task Manager ---")
        print("1. Add task")
        print("2. Mark task as complete")
        print("3. View pending tasks")
        print("4. View progress")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            add_task(tasks, title, description, due_date)
        elif choice == "2":
            mark_task_as_complete(tasks, input("Title of task to complete: "))
        elif choice == "3":
            view_pending_tasks(tasks)
        elif choice == "4":
            print(f"Progress: {calculate_progress(tasks):.1f}% complete")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
