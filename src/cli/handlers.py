"""CLI operation handlers."""
from src.services.task_manager import TaskManager
from src.cli.formatters import format_task_list


def add_task(task_manager: TaskManager) -> None:
    """Handler for adding a new task.

    Args:
        task_manager: TaskManager instance to use
    """
    print("\n=== Add New Task ===")

    # Get title with validation
    while True:
        title = input("Enter task title: ").strip()
        if title:
            break
        print("Error: Task title cannot be empty.")

    # Get description (optional)
    description = input("Enter description (optional): ")

    # Create task
    task = task_manager.add(title, description)
    print(f"\n[SUCCESS] Task created with ID: {task.id}")


def view_tasks(task_manager: TaskManager) -> None:
    """Handler for viewing all tasks.

    Args:
        task_manager: TaskManager instance to use
    """
    tasks = task_manager.get_all()

    if not tasks:
        print("\nNo tasks found. Add a task to get started!")
        return

    formatted_list = format_task_list(tasks)
    print(f"\n{formatted_list}")


def update_task(task_manager: TaskManager) -> None:
    """Handler for updating a task.

    Args:
        task_manager: TaskManager instance to use
    """
    print("\n=== Update Task ===")

    # Get task ID with validation
    while True:
        task_id_str = input("Enter task ID: ")
        try:
            task_id = int(task_id_str)
            break
        except ValueError:
            print("Error: Please enter a valid numeric ID.")

    # Check if task exists
    task = task_manager.get_by_id(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    # Show current values and get new ones
    print(f"Current title: {task.title}")
    new_title = input("Enter new title (or press Enter to keep): ").strip()

    print(f"Current description: {task.description}")
    new_description = input("Enter new description (or press Enter to keep): ")

    # Update task
    title_to_update = new_title if new_title else None
    description_to_update = new_description if new_description != "" else None

    # Only update description if user actually entered something (not just pressed Enter)
    if new_description == "":
        description_to_update = None

    success = task_manager.update(task_id, title_to_update, description_to_update)

    if success:
        print(f"\n[SUCCESS] Task {task_id} updated successfully")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def delete_task(task_manager: TaskManager) -> None:
    """Handler for deleting a task.

    Args:
        task_manager: TaskManager instance to use
    """
    print("\n=== Delete Task ===")

    # Get task ID with validation
    while True:
        task_id_str = input("Enter task ID: ")
        try:
            task_id = int(task_id_str)
            break
        except ValueError:
            print("Error: Please enter a valid numeric ID.")

    # Delete task
    success = task_manager.delete(task_id)

    if success:
        print(f"\n[SUCCESS] Task {task_id} deleted successfully")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def toggle_status(task_manager: TaskManager) -> None:
    """Handler for toggling a task's completion status.

    Args:
        task_manager: TaskManager instance to use
    """
    print("\n=== Toggle Task Status ===")

    # Get task ID with validation
    while True:
        task_id_str = input("Enter task ID: ")
        try:
            task_id = int(task_id_str)
            break
        except ValueError:
            print("Error: Please enter a valid numeric ID.")

    # Get task to show new status
    task = task_manager.get_by_id(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    # Toggle status
    success = task_manager.toggle_status(task_id)

    if success:
        new_status = "complete" if task.is_complete else "incomplete"
        print(f"\n[SUCCESS] Task {task_id} marked as {new_status}")
    else:
        print(f"Error: Task with ID {task_id} not found.")
