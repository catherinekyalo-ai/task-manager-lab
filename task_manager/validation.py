from datetime import datetime


def validate_task_title(title):
    """Title must be 1-50 characters. Raises ValueError if invalid."""
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    if len(title.strip()) > 50:
        raise ValueError("Title must be 50 characters or fewer.")
    return True


def validate_task_description(description):
    """Description must be 1-200 characters. Raises ValueError if invalid."""
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    if len(description.strip()) > 200:
        raise ValueError("Description must be 200 characters or fewer.")
    return True


def validate_due_date(due_date):
    """Due date must be a real date in YYYY-MM-DD format. Raises ValueError if invalid."""
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be a valid date in YYYY-MM-DD format.")
    return True
