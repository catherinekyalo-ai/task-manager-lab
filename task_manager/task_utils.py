from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


def add_task(tasks, title, description, due_date):
    """Validate input, then add a new task. Returns True if added."""
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as error:
        print(f"Error: {error}")
        return False
    tasks.append(
        {
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date,
            "completed": False,
        }
    )
    print("Task added successfully!")
    return True


def mark_task_as_complete(tasks, task_number):
    """Mark the task with the given 1-based number as complete."""
    try:
        index = int(task_number) - 1
    except ValueError:
        print("Error: Please enter a valid task number.")
        return False
    if index < 0 or index >= len(tasks):
        print("Error: Task number does not exist.")
        return False
    if tasks[index]["completed"]:
        print("Error: Task is already complete.")
        return False
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True


def view_pending_tasks(tasks):
    """Print and return all tasks that are not completed."""
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return pending
    print("Pending tasks:")
    for number, task in enumerate(tasks, start=1):
        if not task["completed"]:
            print(f"{number}. {task['title']} - {task['description']} (due {task['due_date']})")
    return pending


def calculate_progress(tasks):
    """Return the percentage of tasks completed (0 if there are no tasks)."""
    if not tasks:
        return 0.0
    done = sum(1 for task in tasks if task["completed"])
    return done / len(tasks) * 100
