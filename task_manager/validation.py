from datetime import datetime


def validate_task_title(title):
    """Title must be a non-empty string of at most 50 characters."""
    if not isinstance(title, str) or not title.strip():
        print("Error: Title cannot be empty.")
        return False
    if len(title.strip()) > 50:
        print("Error: Title must be 50 characters or fewer.")
        return False
    return True


def validate_task_description(description):
    """Description must be a non-empty string of at most 200 characters."""
    if not isinstance(description, str) or not description.strip():
        print("Error: Description cannot be empty.")
        return False
    if len(description.strip()) > 200:
        print("Error: Description must be 200 characters or fewer.")
        return False
    return True


def validate_due_date(due_date):
    """Due date must be a real date in YYYY-MM-DD format."""
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        print("Error: Due date must be a valid date in YYYY-MM-DD format.")
        return False
