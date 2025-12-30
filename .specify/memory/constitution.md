<!--
  SYNC IMPACT REPORT
  ==================
  Version change: 0.0.0 → 1.0.0 (initial ratification)

  Modified principles: N/A (initial constitution)

  Added sections:
    - Core Principles (6 principles)
    - Technical Constraints
    - Development Workflow
    - Governance

  Removed sections: N/A

  Templates requiring updates:
    ✅ .specify/templates/plan-template.md - No changes required (generic)
    ✅ .specify/templates/spec-template.md - No changes required (generic)
    ✅ .specify/templates/tasks-template.md - No changes required (generic)

  Follow-up TODOs: None
-->

# Todo In-Memory Python Console Application Constitution

## Core Principles

### I. Spec-Driven Development

All behavior MUST originate from written specifications. No assumptions or implicit logic are permitted.

- Every feature MUST be documented in a specification before implementation
- Implementation decisions MUST be traceable to a specific specification requirement
- No feature exists without a corresponding spec entry
- Changes to behavior require spec amendment first, then implementation

**Rationale**: Ensures complete traceability from requirements to code, enabling reviewers
to validate the agentic workflow and verify developer intent through specifications.

### II. In-Memory Only Storage

The application MUST store all data strictly in memory with no persistence layer.

- ❌ No file system storage (no JSON, CSV, SQLite, or any file-based storage)
- ❌ No database connections (no SQL, NoSQL, or embedded databases)
- ❌ No caching layers (no Redis, Memcached, or disk cache)
- ❌ No persistence of any kind between application sessions
- ✅ All task data exists only during runtime execution

**Rationale**: Phase I Hackathon constraint enforces focus on core functionality and
spec-driven workflow rather than infrastructure complexity.

### III. Agentic Code Generation

All code MUST be generated via Claude Code. No manual code editing is permitted.

- ❌ No direct coding by the developer
- ❌ No manual code editing at any stage
- ✅ All changes occur through spec refinement and agentic generation
- ✅ Code modifications require spec update → regeneration workflow

**Rationale**: Demonstrates fully agentic development workflow where Claude Code acts as
the sole code author, validating the spec-driven development process.

### IV. Console Interface Only

The application MUST use command-line/console interface exclusively.

- ❌ No UI frameworks or web interfaces
- ❌ No GUI libraries or graphical components
- ❌ No REST APIs or network interfaces
- ✅ All interaction via stdin/stdout/stderr
- ✅ Human-readable console output with clear formatting

**Rationale**: Constrains scope to core functionality, ensuring the hackathon deliverable
focuses on demonstrating spec-driven development rather than interface complexity.

### V. Clean Code Standards

All generated code MUST adhere to clean code principles.

- Clear function and variable naming (self-documenting)
- Single responsibility per function
- Logical separation of concerns
- Readable and maintainable structure
- No dead code or unused logic
- No code comments unless logic is non-obvious

**Rationale**: Even auto-generated code must be reviewable and maintainable. Code quality
reflects specification quality.

### VI. Deterministic Behavior

Given the same inputs, the application MUST behave consistently and predictably.

- Task IDs MUST be unique and sequential
- Operations MUST produce identical results for identical inputs
- Error messages MUST be clear and actionable
- State changes MUST be explicit and traceable

**Rationale**: Predictable behavior enables testing and validation of the spec-driven
workflow without debugging non-deterministic edge cases.

## Technical Constraints

- **Language**: Python 3.13+ (MUST use this version)
- **Runtime/Environment**: UV package manager and runtime
- **Interface**: Console/CLI only
- **Storage**: In-memory only (Python data structures)
- **Dependencies**: Python standard library only (no external packages)
- **Code Generation**: Claude Code exclusively
- **Specification Framework**: Spec-Kit Plus

### Mandatory Features (Five Basic Features)

The application MUST implement all five features:

1. **Add Task**: Create a task with title and description
2. **View Tasks**: Display all tasks with clear status indicators
3. **Update Task**: Modify task title and/or description by ID
4. **Delete Task**: Remove a task by unique ID
5. **Toggle Status**: Mark tasks as complete or incomplete

### Task Data Structure

- Task ID: Unique, sequential, auto-generated integer
- Title: Required string (non-empty)
- Description: Required string (may be empty)
- Status: Complete or Incomplete (boolean)

## Development Workflow

### Agentic Dev Stack Workflow

```
Write Spec → Generate Plan → Break into Tasks → Implement via Claude Code
```

1. **Specification Phase**: Define behavior in spec.md
2. **Planning Phase**: Create implementation plan in plan.md
3. **Task Generation**: Break plan into actionable tasks.md
4. **Implementation**: Execute tasks via Claude Code
5. **Validation**: Verify against specification requirements

### Change Management

- All changes flow through specification updates
- Direct code modifications are prohibited
- Spec refinement triggers regeneration of downstream artifacts

## Governance

### Amendment Procedure

1. Propose amendment with rationale
2. Document impact on existing specifications
3. Update constitution with new version
4. Propagate changes to dependent templates
5. Record in Prompt History Record (PHR)

### Versioning Policy

- **MAJOR**: Backward incompatible principle changes or removals
- **MINOR**: New principles or materially expanded guidance
- **PATCH**: Clarifications, wording, or non-semantic refinements

### Compliance Requirements

- All PRs/reviews MUST verify compliance with this constitution
- Complexity MUST be justified against principles
- Violations require documented exception with rationale

### Success Criteria Verification

- All five required features work correctly via console
- Tasks managed entirely in memory
- Project structure matches required layout
- Specs clearly show evolution and refinement
- Implementation strictly follows specifications
- Reviewers can validate full agentic workflow from specs to code

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30
