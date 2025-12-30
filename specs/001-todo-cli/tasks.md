---
description: "Task list for Todo In-Memory Console Application"
---

# Tasks: Todo In-Memory Console Application

**Input**: Design documents from `/specs/001-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md

**Tests**: No test framework for Phase I (manual console testing only)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/` at repository root
- Paths use forward slashes for cross-platform compatibility

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create src/ directory structure (models/, services/, cli/)
- [x] T002 Create pyproject.toml for UV with Python 3.13+ requirement
- [x] T003 [P] Create src/__init__.py package marker
- [x] T004 [P] Create src/models/__init__.py package marker
- [x] T005 [P] Create src/services/__init__.py package marker
- [x] T006 [P] Create src/cli/__init__.py package marker

**Checkpoint**: Project structure ready for implementation

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Implement Task dataclass in src/models/task.py with fields: id (int), title (str), description (str=""), is_complete (bool=False)
- [x] T008 Implement TaskManager class in src/services/task_manager.py with __init__ method initializing _tasks: list[Task] and _next_id: int = 1

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks with title and optional description

**Independent Test**: Run application, select "add task", enter title and description, verify task created with unique ID

### Implementation for User Story 1

- [x] T009 [US1] Implement TaskManager.add(title: str, description: str = "") -> Task method in src/services/task_manager.py that creates Task with _next_id, increments _next_id, appends to _tasks, returns Task
- [x] T010 [US1] Implement add_task handler in src/cli/handlers.py that prompts for title, validates non-empty after strip(), prompts for description, calls TaskManager.add(), displays confirmation with task ID
- [x] T011 [US1] Add title validation in add_task handler: reject empty/whitespace-only titles with error message "Error: Task title cannot be empty."

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can view all tasks with ID, title, description, and status

**Independent Test**: Add several tasks (mix of complete/incomplete), select "view tasks", verify all details displayed with clear status indicators

### Implementation for User Story 2

- [x] T012 [US2] Implement TaskManager.get_all() -> list[Task] method in src/services/task_manager.py that returns copy of _tasks list
- [x] T013 [US2] Implement format_task_list function in src/cli/formatters.py that takes list[Task] and returns formatted string with box drawing characters, showing ID, status ([x] or [ ]), title, description
- [x] T014 [US2] Implement view_tasks handler in src/cli/handlers.py that calls TaskManager.get_all(), handles empty list with message "No tasks found. Add a task to get started!", otherwise calls format_task_list and displays result
- [x] T015 [US2] Add task count summary to format_task_list: show total, complete count, incomplete count at bottom

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task (Priority: P2)

**Goal**: Users can update task title and/or description by ID

**Independent Test**: Create a task, update its title/description, verify changes persist while ID unchanged

### Implementation for User Story 3

- [x] T016 [US3] Implement TaskManager.get_by_id(task_id: int) -> Task | None method in src/services/task_manager.py that searches _tasks for matching ID
- [x] T017 [US3] Implement TaskManager.update(task_id: int, title: str | None, description: str | None) -> bool method in src/services/task_manager.py that finds task, updates non-None fields, returns success
- [x] T018 [US3] Implement update_task handler in src/cli/handlers.py that prompts for ID, validates numeric input, shows current values, prompts for new title (Enter to skip), prompts for new description (Enter to skip), calls TaskManager.update(), displays success/error
- [x] T019 [US3] Add ID validation in update_task handler: catch non-numeric input with error "Error: Please enter a valid numeric ID."
- [x] T020 [US3] Add not-found handling in update_task handler: display "Error: Task with ID {id} not found." when update returns False

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Users can delete tasks by ID

**Independent Test**: Create tasks, delete one by ID, verify it's removed while others remain

### Implementation for User Story 4

- [x] T021 [US4] Implement TaskManager.delete(task_id: int) -> bool method in src/services/task_manager.py that finds task by ID, removes from _tasks, returns success (does NOT decrement _next_id)
- [x] T022 [US4] Implement delete_task handler in src/cli/handlers.py that prompts for ID, validates numeric input, calls TaskManager.delete(), displays success/error
- [x] T023 [US4] Add ID validation in delete_task handler: catch non-numeric input with error "Error: Please enter a valid numeric ID."
- [x] T024 [US4] Add not-found handling in delete_task handler: display "Error: Task with ID {id} not found." when delete returns False

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Toggle Task Status (Priority: P2)

**Goal**: Users can mark tasks as complete or incomplete

**Independent Test**: Create task, mark complete, verify status change, toggle back to incomplete

### Implementation for User Story 5

- [x] T025 [US5] Implement TaskManager.toggle_status(task_id: int) -> bool method in src/services/task_manager.py that finds task, flips is_complete flag, returns success
- [x] T026 [US5] Implement toggle_status handler in src/cli/handlers.py that prompts for ID, validates numeric input, calls TaskManager.toggle_status(), displays success with new status
- [x] T027 [US5] Add ID validation in toggle_status handler: catch non-numeric input with error "Error: Please enter a valid numeric ID."
- [x] T028 [US5] Add not-found handling in toggle_status handler: display "Error: Task with ID {id} not found." when toggle returns False

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Menu system, error handling, and final integration

- [x] T029 Implement display_menu function in src/cli/menu.py that displays menu with box drawing characters: "1. Add Task", "2. View All Tasks", "3. Update Task", "4. Delete Task", "5. Toggle Task Status", "6. Exit"
- [x] T030 Implement get_menu_choice function in src/cli/menu.py that prompts "Enter your choice (1-6): ", validates integer 1-6, returns choice or shows "Invalid choice. Please enter a number 1-6."
- [x] T031 Implement main_loop function in src/cli/menu.py that creates TaskManager instance, loops display_menu + get_menu_choice, dispatches to handlers, handles exit (option 6)
- [x] T032 Implement main entry point in src/main.py that imports and calls main_loop from cli.menu, includes if __name__ == "__main__" guard
- [x] T033 Add exit message in main_loop: display "Goodbye! Your tasks have not been saved (in-memory only)." before exiting
- [x] T034 Test all acceptance scenarios from spec.md: verify US1 scenarios 1-4, US2 scenarios 1-3, US3 scenarios 1-3, US4 scenarios 1-3, US5 scenarios 1-3

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Depends on TaskManager.get_by_id from Phase 5 setup OR can implement get_by_id in Phase 5
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before CLI handlers
- Core implementation before error handling
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks (T003-T006) marked [P] can run in parallel
- User Stories 1 and 2 can be developed in parallel after Foundational phase
- User Stories 3, 4, 5 can be developed in parallel after Foundational phase (US3 needs get_by_id but can implement it)
- Within each story, independent file creation can run in parallel

---

## Parallel Example: Setup Phase

```bash
# Launch all package markers together:
Task: "Create src/__init__.py package marker"
Task: "Create src/models/__init__.py package marker"
Task: "Create src/services/__init__.py package marker"
Task: "Create src/cli/__init__.py package marker"
```

---

## Parallel Example: User Stories

```bash
# After Foundational phase complete, launch User Stories 1 and 2 together:
Task: "Implement TaskManager.add method for US1"
Task: "Implement TaskManager.get_all method for US2"

# Then launch their handlers in parallel:
Task: "Implement add_task handler for US1"
Task: "Implement view_tasks handler for US2"
```

---

## Implementation Strategy

### MVP First (User Stories 1 and 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test US1 and US2 independently
6. Deploy/demo if ready (basic todo app functional)

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → (Can capture tasks)
3. Add User Story 2 → Test independently → (MVP: Can add and view!)
4. Add User Story 3 → Test independently → (Can edit)
5. Add User Story 4 → Test independently → (Can delete)
6. Add User Story 5 → Test independently → (Full lifecycle)
7. Add Polish (Phase 8) → Complete application
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (T009-T011)
   - Developer B: User Story 2 (T012-T015)
   - Developer C: User Story 3 (T016-T020)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- No test framework - validation via manual console testing per acceptance scenarios
- Task IDs never reused (spec requirement)
- All code generated via Claude Code (no manual editing)

---

## Task Count Summary

| Phase | Task Count | Description |
|-------|------------|-------------|
| Phase 1: Setup | 6 | Project structure |
| Phase 2: Foundational | 2 | Task model + TaskManager base |
| Phase 3: US1 (Add) | 3 | Add task functionality |
| Phase 4: US2 (View) | 4 | View tasks functionality |
| Phase 5: US3 (Update) | 5 | Update task functionality |
| Phase 6: US4 (Delete) | 4 | Delete task functionality |
| Phase 7: US5 (Toggle) | 4 | Toggle status functionality |
| Phase 8: Polish | 6 | Menu, integration, testing |
| **Total** | **34** | **All tasks** |

## MVP Scope Recommendation

**Minimum Viable Product**: Complete through Phase 4 (User Stories 1 & 2)
- Tasks T001-T015 (15 tasks)
- Provides: Add tasks + View tasks
- Delivers: Basic functional todo application
- Time estimate: Fastest path to working demo
