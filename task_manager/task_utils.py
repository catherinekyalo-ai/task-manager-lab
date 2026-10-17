from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


def add_task(tasks, title, description, due_date):
    """Validate input, then add a new task. Returns True if added."""
    if not (
        validate_task_title(title)
        and validate_task_description(description)
        and validate_due_date(due_date)
    ):
        return False
    tasks.append(
        {
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date,
            "completed": False,
        }
    )
    print(f"Task '{title.strip()}' added.")
    return True


def mark_task_as_complete(tasks, title):
    """Mark the first matching pending task as complete. Returns True if found."""
    for task in tasks:
        if task["title"].lower() == title.strip().lower() and not task["completed"]:
            task["completed"] = True
            print(f"Task '{task['title']}' marked as complete.")
            return True
    print(f"Error: No pending task found with title '{title}'.")
    return False


def view_pending_tasks(tasks):
    """Print and return all tasks that are not completed."""
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks.")
        return pending
    print("Pending tasks:")
    for i, task in enumerate(pending, start=1):
        print(f"{i}. {task['title']} - {task['description']} (due {task['due_date']})")
    return pending


def calculate_progress(tasks):
    """Return the percentage of tasks completed (0 if there are no tasks)."""
    if not tasks:
        return 0.0
    done = sum(1 for task in tasks if task["completed"])
    return done / len(tasks) * 100
