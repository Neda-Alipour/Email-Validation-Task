# Terminal-Based AI Agent Task: Email Validation

## Overview

This project defines a deterministic, terminal-based task designed for AI agents. The agent must analyze a CSV file containing user records and identify invalid email addresses based on clearly defined rules.

## Task Description

The AI agent is provided with a directory containing a CSV file (`users.csv`). Some records contain invalid email addresses according to the specified validation rules.

## Email Validation Rules

An email is considered valid if it meets the following criteria:

1. It contains exactly one `@` character.
2. The local part (before the `@`) must be non-empty and can contain letters, numbers, dots, underscores, or hyphens.
3. The domain part (after the `@`) must not start or end with a dot, must contain at least one dot, and must not have consecutive dots.
4. No spaces are allowed anywhere in the email.

## Input

* The `data/users.csv` file contains columns: `id`, `name`, and `email`.

## Output Format

The agent should output the IDs of invalid records in the following format:

```
INVALID_IDS: id1,id2,id3,...
```

## Setup

To initialize the task environment, run:

```bash
python setup.py
```

## Validation

After the agent produces its output, run the following command to check correctness:

```bash
python validate.py
```

The task will pass if the output matches the expected invalid IDs exactly.

## Why This Task Matters

This task demonstrates the ability to design deterministic, terminal-based challenges for AI agents, ensuring clarity, consistency, and robust evaluation.
