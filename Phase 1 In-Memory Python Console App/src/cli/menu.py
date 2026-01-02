"""Menu display and main loop."""
from src.services.task_manager import TaskManager
from src.cli.handlers import add_task, view_tasks, update_task, delete_task, toggle_status


def display_menu() -> None:
    """Display the main menu."""
    print("\n" + "="*40)
    print("       TODO LIST MANAGER")
    print("="*40)
    print("  1. Add Task")
    print("  2. View All Tasks")
    print("  3. Update Task")
    print("  4. Delete Task")
    print("  5. Toggle Task Status")
    print("  6. Exit")
    print("="*40)


def get_menu_choice() -> int:
    """Prompt for and validate menu choice.

    Returns:
        Valid menu choice (1-6)
    """
    while True:
        choice_str = input("\nEnter your choice (1-6): ")
        try:
            choice = int(choice_str)
            if 1 <= choice <= 6:
                return choice
            print("Invalid choice. Please enter a number 1-6.")
        except ValueError:
            print("Invalid choice. Please enter a number 1-6.")


def main_loop() -> None:
    """Main application loop."""
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            add_task(task_manager)
        elif choice == 2:
            view_tasks(task_manager)
        elif choice == 3:
            update_task(task_manager)
        elif choice == 4:
            delete_task(task_manager)
        elif choice == 5:
            toggle_status(task_manager)
        elif choice == 6:
            print("\nGoodbye! Your tasks have not been saved (in-memory only).")
            break
