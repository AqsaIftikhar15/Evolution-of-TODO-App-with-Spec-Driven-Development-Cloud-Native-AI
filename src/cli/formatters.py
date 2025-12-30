"""Output formatting utilities."""
from src.models.task import Task


def format_task_list(tasks: list[Task]) -> str:
    """Format a list of tasks for display.

    Args:
        tasks: List of tasks to format

    Returns:
        Formatted string with box drawing characters
    """
    if not tasks:
        return ""

    lines = []
    lines.append("="*60)
    lines.append("                     YOUR TASKS")
    lines.append("="*60)

    for i, task in enumerate(tasks):
        status_icon = "[x]" if task.is_complete else "[ ]"
        lines.append(f" ID: {task.id}  {status_icon} {task.title}")

        desc = task.description if task.description else "(none)"
        lines.append(f"        Description: {desc}")

        # Add separator between tasks (not after last one)
        if i < len(tasks) - 1:
            lines.append("-"*60)

    lines.append("="*60)

    # Add task count summary
    complete_count = sum(1 for task in tasks if task.is_complete)
    incomplete_count = len(tasks) - complete_count
    lines.append(f"\nTotal: {len(tasks)} task{'s' if len(tasks) != 1 else ''} "
                 f"({complete_count} complete, {incomplete_count} incomplete)")

    return "\n".join(lines)
