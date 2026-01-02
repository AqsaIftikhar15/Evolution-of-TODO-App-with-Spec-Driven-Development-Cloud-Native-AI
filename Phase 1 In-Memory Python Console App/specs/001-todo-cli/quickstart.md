# Quickstart: Todo In-Memory Console Application

**Branch**: `001-todo-cli` | **Date**: 2025-12-30

## Prerequisites

- Python 3.13+
- UV package manager

## Installation

```bash
# Clone repository (if not already done)
cd "hackathon 2"

# Ensure UV is installed
uv --version

# Sync dependencies (creates virtual environment)
uv sync
```

## Running the Application

```bash
# Run with UV
uv run python -m src.main

# Or activate virtual environment and run directly
source .venv/bin/activate  # Linux/macOS
# OR
.venv\Scripts\activate     # Windows

python -m src.main
```

## Usage

### Main Menu

When you start the application, you'll see:

```text
╔══════════════════════════════════════╗
║       TODO LIST MANAGER              ║
╠══════════════════════════════════════╣
║  1. Add Task                         ║
║  2. View All Tasks                   ║
║  3. Update Task                      ║
║  4. Delete Task                      ║
║  5. Toggle Task Status               ║
║  6. Exit                             ║
╚══════════════════════════════════════╝

Enter your choice (1-6):
```

### Adding a Task

1. Select option `1`
2. Enter task title (required)
3. Enter description (optional, press Enter to skip)

```text
Enter your choice (1-6): 1

=== Add New Task ===
Enter task title: Buy groceries
Enter description (optional): Milk, eggs, bread

✓ Task created with ID: 1
```

### Viewing Tasks

Select option `2` to see all tasks:

```text
╔══════════════════════════════════════════════════════════╗
║                     YOUR TASKS                           ║
╠══════════════════════════════════════════════════════════╣
║ ID: 1  [ ] Buy groceries                                 ║
║        Description: Milk, eggs, bread                    ║
╚══════════════════════════════════════════════════════════╝

Total: 1 task (0 complete, 1 incomplete)
```

### Updating a Task

1. Select option `3`
2. Enter the task ID
3. Enter new title (or press Enter to keep current)
4. Enter new description (or press Enter to keep current)

```text
Enter your choice (1-6): 3

=== Update Task ===
Enter task ID: 1
Current title: Buy groceries
Enter new title (or press Enter to keep): Buy organic groceries
Current description: Milk, eggs, bread
Enter new description (or press Enter to keep):

✓ Task 1 updated successfully
```

### Deleting a Task

1. Select option `4`
2. Enter the task ID to delete

```text
Enter your choice (1-6): 4

=== Delete Task ===
Enter task ID: 1

✓ Task 1 deleted successfully
```

### Toggling Task Status

1. Select option `5`
2. Enter the task ID to toggle

```text
Enter your choice (1-6): 5

=== Toggle Task Status ===
Enter task ID: 1

✓ Task 1 marked as complete
```

### Exiting

Select option `6` to exit gracefully:

```text
Enter your choice (1-6): 6

Goodbye! Your tasks have not been saved (in-memory only).
```

## Important Notes

- **No Persistence**: All tasks are stored in memory only. When you exit, all data is lost.
- **Sequential IDs**: Task IDs are assigned sequentially (1, 2, 3...) and are never reused.
- **Single Session**: This is a single-user, single-session application.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `uv sync` to install dependencies |
| `command not found: uv` | Install UV: `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Invalid Python version | Ensure Python 3.13+ is installed |

## Project Structure

```text
src/
├── main.py              # Entry point
├── models/
│   └── task.py          # Task dataclass
├── services/
│   └── task_manager.py  # Business logic
└── cli/
    ├── menu.py          # Menu display
    ├── handlers.py      # Operation handlers
    └── formatters.py    # Output formatting
```
