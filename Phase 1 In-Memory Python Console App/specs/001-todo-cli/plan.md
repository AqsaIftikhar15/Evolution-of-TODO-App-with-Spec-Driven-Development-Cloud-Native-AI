# Implementation Plan: Todo In-Memory Console Application

**Branch**: `001-todo-cli` | **Date**: 2025-12-30 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-cli/spec.md`

## Summary

Build a command-line todo application in Python 3.13+ that manages tasks entirely in memory. The application provides five core operations (add, view, update, delete, toggle status) through a menu-driven console interface. All code is generated via Claude Code following the spec-driven agentic workflow.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (no external packages)
**Storage**: In-memory only (Python list/dict data structures)
**Testing**: Manual console testing (no test framework for Phase I)
**Target Platform**: Cross-platform console (Windows/Linux/macOS)
**Project Type**: Single project (CLI application)
**Performance Goals**: Interactive response (<1 second per operation)
**Constraints**: No persistence, no external dependencies, stdlib only
**Scale/Scope**: Single-user, single-session, unlimited tasks (memory-bound)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Spec-Driven Development | PASS | All features defined in spec.md with acceptance scenarios |
| II. In-Memory Only Storage | PASS | No persistence planned; Python data structures only |
| III. Agentic Code Generation | PASS | All code to be generated via Claude Code |
| IV. Console Interface Only | PASS | Menu-driven CLI; no GUI/web/API |
| V. Clean Code Standards | PASS | Plan includes modular structure with separation of concerns |
| VI. Deterministic Behavior | PASS | Sequential IDs, predictable operations defined |

**Gate Status**: PASS - All constitution principles satisfied.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py          # Package marker
├── main.py              # Application entry point, main menu loop
├── models/
│   ├── __init__.py
│   └── task.py          # Task dataclass definition
├── services/
│   ├── __init__.py
│   └── task_manager.py  # TaskManager class (add, get, update, delete, toggle)
└── cli/
    ├── __init__.py
    ├── menu.py          # Menu display and navigation
    ├── handlers.py      # Operation handlers (add, view, update, delete, toggle)
    └── formatters.py    # Output formatting utilities
```

**Structure Decision**: Single project structure selected. Minimal module separation maintains clean code principles while avoiding over-engineering for this scope.

## Complexity Tracking

> No violations detected. All design choices align with constitution principles.

| Aspect | Decision | Justification |
|--------|----------|---------------|
| Module count | 3 modules (models, services, cli) | Minimum viable separation of concerns |
| External deps | None | Constitution mandates stdlib only |
| Data structure | Python list + dataclass | Simplest in-memory solution |

## Architecture Overview

### Component Diagram

```text
┌─────────────────────────────────────────────────────────┐
│                      main.py                            │
│                   (Entry Point)                         │
│                        │                                │
│                        ▼                                │
│  ┌─────────────────────────────────────────────────┐   │
│  │                  cli/menu.py                     │   │
│  │            (Menu Display & Loop)                 │   │
│  └─────────────────────────────────────────────────┘   │
│                        │                                │
│                        ▼                                │
│  ┌─────────────────────────────────────────────────┐   │
│  │               cli/handlers.py                    │   │
│  │         (Operation Handlers)                     │   │
│  │   add_task | view_tasks | update_task |          │   │
│  │   delete_task | toggle_status                    │   │
│  └─────────────────────────────────────────────────┘   │
│                        │                                │
│                        ▼                                │
│  ┌─────────────────────────────────────────────────┐   │
│  │           services/task_manager.py               │   │
│  │              (Business Logic)                    │   │
│  │   TaskManager: add, get_all, get_by_id,          │   │
│  │   update, delete, toggle_status                  │   │
│  └─────────────────────────────────────────────────┘   │
│                        │                                │
│                        ▼                                │
│  ┌─────────────────────────────────────────────────┐   │
│  │              models/task.py                      │   │
│  │            (Data Structure)                      │   │
│  │   Task: id, title, description, is_complete      │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

1. **User Input** → `main.py` starts menu loop
2. **Menu Selection** → `cli/menu.py` displays options, captures choice
3. **Handler Dispatch** → `cli/handlers.py` processes user choice
4. **Business Logic** → `services/task_manager.py` executes operation
5. **Data Access** → `models/task.py` provides Task structure
6. **Output** → `cli/formatters.py` formats result for display

## Requirement Traceability Matrix

| FR ID | Requirement | Implementation Component | User Story |
|-------|-------------|-------------------------|------------|
| FR-001 | Add task with title/description | `handlers.add_task()` → `TaskManager.add()` | US1 |
| FR-002 | Sequential unique IDs | `TaskManager._next_id` counter | US1 |
| FR-003 | Display all tasks | `handlers.view_tasks()` → `TaskManager.get_all()` | US2 |
| FR-004 | Update task by ID | `handlers.update_task()` → `TaskManager.update()` | US3 |
| FR-005 | Delete task by ID | `handlers.delete_task()` → `TaskManager.delete()` | US4 |
| FR-006 | Toggle task status | `handlers.toggle_status()` → `TaskManager.toggle()` | US5 |
| FR-007 | Error for non-existent ID | All handlers + TaskManager validation | US3,4,5 |
| FR-008 | Error for invalid input | Input validation in handlers | All |
| FR-009 | Menu-driven interface | `cli/menu.py` | All |
| FR-010 | Graceful exit | Menu option 6 + exit handler | All |
| FR-011 | In-memory only | `TaskManager._tasks: list[Task]` | All |
| FR-012 | Default incomplete status | `Task(is_complete=False)` | US1 |

## Implementation Phases

### Phase 1: Foundation (Setup + Core Model)

**Goal**: Project structure and Task data model

1. Create project directory structure
2. Initialize `pyproject.toml` for UV
3. Implement `models/task.py` with Task dataclass
4. Create package `__init__.py` files

**Deliverables**: Runnable project skeleton with Task model

### Phase 2: Business Logic (TaskManager)

**Goal**: Core task operations without UI

1. Implement `services/task_manager.py`
2. TaskManager class with:
   - `add(title, description) -> Task`
   - `get_all() -> list[Task]`
   - `get_by_id(id) -> Task | None`
   - `update(id, title, description) -> bool`
   - `delete(id) -> bool`
   - `toggle_status(id) -> bool`
3. Sequential ID generation logic

**Deliverables**: Fully functional TaskManager (testable via REPL)

### Phase 3: CLI Layer (Menu + Handlers)

**Goal**: User-facing console interface

1. Implement `cli/menu.py` with main loop
2. Implement `cli/handlers.py` with operation handlers
3. Implement `cli/formatters.py` for output formatting
4. Connect handlers to TaskManager

**Deliverables**: Complete interactive CLI application

### Phase 4: Polish (Error Handling + UX)

**Goal**: Production-ready error handling and user experience

1. Add input validation for all handlers
2. Implement clear error messages
3. Add visual status indicators (e.g., [x] complete, [ ] incomplete)
4. Add confirmation messages for operations
5. Handle edge cases (empty list, invalid IDs, etc.)

**Deliverables**: Polished, user-friendly application

### Phase 5: Integration (Entry Point)

**Goal**: Executable application

1. Implement `main.py` entry point
2. Wire all components together
3. Add graceful exit handling
4. Verify all acceptance scenarios

**Deliverables**: Complete, runnable todo application

## Menu Interface Design

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

Enter your choice (1-6): _
```

## Task Display Format

```text
╔══════════════════════════════════════════════════════════╗
║                     YOUR TASKS                           ║
╠══════════════════════════════════════════════════════════╣
║ ID: 1  [x] Buy groceries                                 ║
║        Description: Milk, eggs, bread                    ║
╠──────────────────────────────────────────────────────────╣
║ ID: 2  [ ] Call mom                                      ║
║        Description: (none)                               ║
╚══════════════════════════════════════════════════════════╝

Total: 2 tasks (1 complete, 1 incomplete)
```

## Error Message Standards

| Scenario | Message |
|----------|---------|
| Empty title | "Error: Task title cannot be empty." |
| Invalid ID format | "Error: Please enter a valid numeric ID." |
| ID not found | "Error: Task with ID {id} not found." |
| Empty task list | "No tasks found. Add a task to get started!" |
| Invalid menu choice | "Invalid choice. Please enter a number 1-6." |

## Validation Rules

| Field | Rule | Error Response |
|-------|------|----------------|
| Title | Non-empty string after strip() | Prompt to re-enter |
| Description | Any string (empty allowed) | N/A |
| Task ID (input) | Positive integer | Show format error |
| Task ID (lookup) | Must exist in collection | Show not found error |
| Menu choice | Integer 1-6 | Show invalid choice error |

## Dependencies

**Runtime**: Python 3.13+
**Build**: UV package manager
**External Packages**: None (stdlib only)

**Standard Library Modules Used**:
- `dataclasses` - Task model definition
- `typing` - Type hints

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Scope creep | Low | Medium | Strict adherence to spec |
| ID overflow | Very Low | Low | Python int has no practical limit |
| Memory exhaustion | Very Low | Medium | Acceptable for hackathon scope |
| Input encoding | Low | Low | Accept all printable characters |

## Next Steps

1. Run `/sp.tasks` to generate detailed task breakdown
2. Execute tasks via Claude Code implementation
3. Validate against acceptance scenarios in spec
