# Terminal-Based AI Agent Task: Email Validation

## Overview
This project defines a deterministic, terminal-based task designed for AI agents.
The agent must analyze a CSV file containing user records and identify invalid email addresses
based on clearly defined rules.

## Task Description
The agent is provided with access to a directory containing a CSV file (`users.csv`).
Some records contain invalid email addresses.

The agent must:
- Read the input file
- Identify all invalid email addresses
- Output the corresponding user IDs in a strict format

## Email Validation Rules
An email is considered invalid if:
- It does not contain exactly one "@" character
- OR it does not contain at least one "." after the "@"

## Input
- `data/users.csv` with columns: `id`, `name`, `email`

## Output Format
INVALID_IDS: id1,id2,id3

IDs must be:
- Unique
- Sorted in ascending order

## Setup
Run the following command to initialize the task environment:

```bash
python setup.py


Validation rules are defined in a shared module and covered by adversarial self-tests to ensure consistency between specification and evaluation.