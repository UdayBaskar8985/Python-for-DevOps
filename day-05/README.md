# Day-05: Command Line Arguments & Environment Variables

## Overview

Today, I learned how to pass values to a Python program using **Command Line Arguments** instead of hardcoding values.

Python provides the built-in `sys` module to access command line arguments.

## 1. sys Module

```python
import sys
```

`sys.argv` stores the arguments passed from the command line.

## 2. Understanding sys.argv

If we run:

```bash
python3 calculator.py add 10 20
```

Then:

```text
sys.argv[0] → calculator.py
sys.argv[1] → add
sys.argv[2] → 10
sys.argv[3] → 20
```

**Important:** Command line arguments are received as strings, so numbers must be converted using `int()`.

## 3. Simple Calculator

```python
import sys

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

operation = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

if operation == "add":
    print(add(num1, num2))

if operation == "sub":
    print(sub(num1, num2))

if operation == "mul":
    print(mul(num1, num2))
```

Run:

```bash
python3 calculator.py add 10 20
```

Output:

```text
30
```

## Key Learning

- `sys` is a built-in Python module.
- `sys.argv` is used to read command line arguments.
- Arguments are received as strings.
- Use `int()` to convert strings into numbers.
- Command line arguments make scripts flexible and reusable.

## DevOps Use Cases

Command line arguments can be used to pass:

- Environment names
- Server names
- File paths
- Application versions
- User inputs

This is useful for creating **reusable DevOps automation scripts**.
