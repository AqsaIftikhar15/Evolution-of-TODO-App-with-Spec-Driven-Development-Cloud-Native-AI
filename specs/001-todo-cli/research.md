# Research: Todo In-Memory Console Application

**Branch**: `001-todo-cli` | **Date**: 2025-12-30
**Phase**: 0 - Research & Discovery

## Research Summary

All technical decisions are predetermined by the constitution and specification. No external research was required as the project uses only Python standard library components.

## Decisions Made

### 1. Data Structure for Task Storage

**Decision**: Python `list[Task]` with `dataclass` for Task model

**Rationale**:
- Simplest in-memory solution
- `dataclass` provides clean, immutable-friendly structure
- List maintains insertion order (by ID)
- No external dependencies required

**Alternatives Considered**:
- `dict[int, Task]` - Faster lookup by ID, but adds complexity
- Named tuple - Less flexible for potential future changes
- Plain dict - Loses type safety benefits

### 2. ID Generation Strategy

**Decision**: Sequential integer counter starting at 1, never reused

**Rationale**:
- Matches spec requirement for "unique, sequential integer ID"
- Simple `_next_id` instance variable in TaskManager
- IDs persist even after deletion (spec: "deleted ID 3 means next task is still ID 4+")

**Alternatives Considered**:
- UUID - Overkill for single-session, in-memory app
- Timestamp-based - Not sequential as required
- Reusable IDs - Explicitly rejected by spec

### 3. CLI Framework

**Decision**: Pure Python input/print (no framework)

**Rationale**:
- Constitution mandates stdlib only
- Simple menu loop sufficient for 6 options
- No need for argument parsing (interactive-only)

**Alternatives Considered**:
- `argparse` - Good for CLI args, but app is interactive menu-based
- `curses` - Adds complexity without clear benefit
- Third-party (click, typer) - Violates stdlib-only constraint

### 4. Module Organization

**Decision**: Three-module structure (models, services, cli)

**Rationale**:
- Minimum viable separation of concerns
- Follows clean code principle of single responsibility
- Easy to navigate and understand

**Alternatives Considered**:
- Single file - Violates separation of concerns
- More granular modules - Over-engineering for scope

## Unresolved Items

None. All technical decisions are clear from constitution and specification.

## References

- Python 3.13 `dataclasses` documentation
- Python 3.13 `typing` module for type hints
- UV package manager documentation
