"""Task management service."""
from src.models.task import Task


class TaskManager:
    """Manages the in-memory collection of tasks.

    Attributes:
        _tasks: Internal storage of all tasks
        _next_id: Counter for next available ID (starts at 1)
    """

    def __init__(self):
        """Initialize TaskManager with empty task list and ID counter at 1."""
        self._tasks: list[Task] = []
        self._next_id: int = 1

    def add(self, title: str, description: str = "") -> Task:
        """Create and add a new task.

        Args:
            title: Task title (required, non-empty)
            description: Optional task description

        Returns:
            The newly created Task
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            is_complete=False
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all(self) -> list[Task]:
        """Get all tasks.

        Returns:
            Copy of the tasks list
        """
        return self._tasks.copy()

    def get_by_id(self, task_id: int) -> Task | None:
        """Find a task by ID.

        Args:
            task_id: ID of the task to find

        Returns:
            Task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update(self, task_id: int, title: str | None, description: str | None) -> bool:
        """Update a task's title and/or description.

        Args:
            task_id: ID of the task to update
            title: New title (None to keep current)
            description: New description (None to keep current)

        Returns:
            True if task was found and updated, False otherwise
        """
        task = self.get_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return True

    def delete(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if task was found and deleted, False otherwise
        """
        task = self.get_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        # Note: Do NOT decrement _next_id - IDs are never reused
        return True

    def toggle_status(self, task_id: int) -> bool:
        """Toggle a task's completion status.

        Args:
            task_id: ID of the task to toggle

        Returns:
            True if task was found and toggled, False otherwise
        """
        task = self.get_by_id(task_id)
        if task is None:
            return False

        task.is_complete = not task.is_complete
        return True
