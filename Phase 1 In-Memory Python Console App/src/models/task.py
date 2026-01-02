"""Task data model."""
from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo item.

    Attributes:
        id: Unique sequential integer identifier (auto-generated, immutable)
        title: Required text describing the task (user-provided, mutable)
        description: Optional additional details (user-provided, mutable, may be empty)
        is_complete: Completion status (mutable, defaults to False)
    """
    id: int
    title: str
    description: str = ""
    is_complete: bool = False
