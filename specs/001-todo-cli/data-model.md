# Data Model: Todo In-Memory Console Application

**Branch**: `001-todo-cli` | **Date**: 2025-12-30
**Phase**: 1 - Design & Contracts

## Entity Definitions

### Task

The core entity representing a single todo item.

| Field | Type | Required | Mutable | Default | Description |
|-------|------|----------|---------|---------|-------------|
| `id` | `int` | Yes | No | Auto-generated | Unique sequential identifier (1, 2, 3...) |
| `title` | `str` | Yes | Yes | N/A | Task title (non-empty after strip) |
| `description` | `str` | Yes | Yes | `""` | Optional task details (may be empty) |
| `is_complete` | `bool` | Yes | Yes | `False` | Completion status |

**Validation Rules**:
- `id`: Positive integer, auto-assigned, immutable after creation
- `title`: Must be non-empty string after `strip()`; whitespace-only rejected
- `description`: Any string allowed, including empty
- `is_complete`: Boolean only; defaults to `False` on creation

**Python Implementation** (dataclass):

```python
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    is_complete: bool = False
```

### TaskManager

The service managing the in-memory task collection.

| Field | Type | Description |
|-------|------|-------------|
| `_tasks` | `list[Task]` | Internal storage of all tasks |
| `_next_id` | `int` | Counter for next available ID (starts at 1) |

**Operations**:

| Method | Signature | Returns | Description |
|--------|-----------|---------|-------------|
| `add` | `(title: str, description: str = "") -> Task` | Created Task | Creates and stores new task |
| `get_all` | `() -> list[Task]` | All tasks | Returns all tasks in ID order |
| `get_by_id` | `(task_id: int) -> Task \| None` | Task or None | Finds task by ID |
| `update` | `(task_id: int, title: str \| None, description: str \| None) -> bool` | Success | Updates task fields |
| `delete` | `(task_id: int) -> bool` | Success | Removes task from collection |
| `toggle_status` | `(task_id: int) -> bool` | Success | Flips is_complete flag |

**Invariants**:
- `_next_id` always equals `max(task.id for task in _tasks) + 1` or `1` if empty
- IDs are never reused (deletion does not decrement `_next_id`)
- `_tasks` list maintains insertion order

## State Transitions

### Task Lifecycle

```text
              ┌─────────────┐
              │   Created   │
              │ (incomplete)│
              └──────┬──────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
    ┌─────────┐ ┌─────────┐ ┌─────────┐
    │ Updated │ │ Toggled │ │ Deleted │
    │ (title/ │ │  (to    │ │(removed)│
    │  desc)  │ │complete)│ │         │
    └────┬────┘ └────┬────┘ └─────────┘
         │           │
         │           ▼
         │      ┌─────────┐
         │      │ Toggled │
         │      │  (to    │
         │      │incomplete│
         │      └────┬────┘
         │           │
         └─────┬─────┘
               │
               ▼
          (continues until deleted)
```

### Status States

| State | `is_complete` | Display |
|-------|---------------|---------|
| Incomplete | `False` | `[ ]` |
| Complete | `True` | `[x]` |

## Relationships

```text
┌─────────────────┐         ┌─────────────────┐
│   TaskManager   │ 1     * │      Task       │
│                 │─────────│                 │
│ - _tasks        │         │ - id            │
│ - _next_id      │         │ - title         │
│                 │         │ - description   │
│ + add()         │         │ - is_complete   │
│ + get_all()     │         │                 │
│ + get_by_id()   │         │                 │
│ + update()      │         │                 │
│ + delete()      │         │                 │
│ + toggle_status()│        │                 │
└─────────────────┘         └─────────────────┘
```

## Data Volume Assumptions

| Metric | Expected Value | Notes |
|--------|----------------|-------|
| Max tasks per session | Unlimited | Bounded only by memory |
| Task title length | No limit | Accepts any length |
| Task description length | No limit | Accepts any length |
| Typical usage | < 100 tasks | Hackathon demo scope |

## Error Conditions

| Operation | Error Condition | Response |
|-----------|-----------------|----------|
| `add` | Empty title | Reject, return error |
| `get_by_id` | ID not found | Return `None` |
| `update` | ID not found | Return `False` |
| `delete` | ID not found | Return `False` |
| `toggle_status` | ID not found | Return `False` |
