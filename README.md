# Python for DevOps - 17 Days Learning Roadmap

This repository contains my notes and hands-on practice for learning **Python for DevOps**.

---

## Day 01 - Introduction to Python, Installation and Configuration

### Topics Covered

- Introduction to Python.
- Python and its role in DevOps.
- Installing Python.
- Setting up a development environment.
- Writing the first Python program.

### Key Learning

Python is widely used in DevOps for:

- Automation
- Infrastructure management
- Cloud operations
- API integration
- File and log processing

---

## Day 02 - Data Types, Strings and Numbers

### Topics Covered

- String data type.
- String manipulation.
- String formatting.
- Regular expressions.
- Numeric data types.
- Integers (`int`).
- Floating-point numbers (`float`).

---

## Day 03 - Keywords and Variables

### Topics Covered

- Understanding Python variables.
- Variable scope and lifetime.
- Variable naming conventions.
- Variable best practices.
- Using variables to store configuration data.

### DevOps Example

Variables can be used to store:

- Server names
- IP addresses
- Environment names
- Application versions

---

## Day 04 - Functions, Modules and Packages

### Topics Covered

- Understanding functions.
- Understanding modules.
- Understanding packages.
- Difference between functions, modules and packages.
- Importing modules and packages.
- Understanding Python workspaces.

---

## Day 05 - Environment Variables and Command Line Arguments

### Topics Covered

- Reading environment variables.
- Writing environment variables.
- Using the `os` module.
- Using the `dotenv` module.
- Securing sensitive information.
- Handling command-line arguments.

### DevOps Example

Creating Python scripts that accept command-line arguments to customize automation tasks.

---

## Day 06 - Operators

### Topics Covered

- Arithmetic operators.
- Comparison operators.
- Logical operators.
- Bitwise operators.
- Assignment operators.

### DevOps Example

Using operators for:

- Calculations
- Comparisons
- Decision making
- Automation logic

---

## Day 07 - Conditional Handling

### Topics Covered

- `if` statements.
- `elif` statements.
- `else` statements.
- Conditional decision making.

### Example

```python
if environment == "production":
    print("Production deployment")
else:
    print("Non-production deployment")
```

---

## Day 08 - Working with Lists (Part 1)

### Topics Covered

- Understanding lists.
- List data structure.
- Creating lists.
- Adding and removing items.
- Common list operations.

### DevOps Example

Managing a list of:

- User accounts
- Servers
- Applications
- Resources

---

## Day 09 - Loops

### Topics Covered

- `for` loops.
- `while` loops.
- `break` statement.
- `continue` statement.

### DevOps Example

Using loops to:

- Process multiple servers.
- Analyze log files.
- Find errors.
- Automate repetitive tasks.

---

## Day 10 - Working with Lists (Part 2)

### Topics Covered

- List comprehensions.
- Nested lists.
- Advanced list operations.

### DevOps Example

Printing files from multiple folders.

---

## Day 11 - Dictionaries and Sets (Project 1)

### Topics Covered

- Dictionaries.
- Key-value pairs.
- Sets.
- Set operations.
- Managing configuration data.

### DevOps Example

Managing server configurations using dictionaries.

Example:

```python
server = {
    "name": "web-server",
    "ip": "192.168.1.10",
    "environment": "production"
}
```

---

## Day 12 - Python Tasks for DevOps: File Operations (Project 2)

### Topics Covered

- File operations.
- Reading files.
- Writing files.
- Updating files.
- Introduction to Boto3.
- Automating file operations.

### DevOps Example

Updating server configuration files based on external notifications.

---

## Day 13 - Python Tasks for DevOps: Automation (Project 3)

### Topics Covered

- Remote task automation using Fabric.
- AWS automation using Boto3.
- Managing EC2 instances.
- Managing S3 buckets.
- Automating cloud infrastructure.

### DevOps Example

Creating a Python script to deploy applications to remote servers.

---

## Day 14 - GitHub-JIRA Integration (Project 4 - Part 1)

### Topics Covered

- Introduction to REST APIs.
- Making HTTP requests using Python.
- Parsing JSON responses.
- Error handling.
- GitHub and JIRA integration.

### Project Example

Creating a Python API that:

1. Listens to a GitHub comment.
2. Processes the request.
3. Creates a ticket in JIRA.

---

## Day 15 - GitHub-JIRA Integration (Project 4 - Part 2)

### Topics Covered

- Introduction to Flask.
- Creating APIs using Python.
- Handling API requests.
- Deploying APIs to a server.

### Project Example

Building and deploying a Python API that integrates GitHub with JIRA.

---

## Day 16 - Python Interview Questions and Answers

### Topics Covered

- Beginner-level Python interview questions.
- Intermediate-level Python interview questions.
- Important Python concepts for interviews.

---

## Day 17 - Advanced Python Interview Questions and Answers

### Topics Covered

- Advanced Python concepts.
- Advanced-level interview questions.
- Python concepts useful for DevOps roles.

---

# Key Takeaways

During this Python for DevOps journey, I learned:

- Python fundamentals.
- Data types and variables.
- Strings and numbers.
- Functions, modules and packages.
- Environment variables.
- Command-line arguments.
- Operators and conditional statements.
- Lists, dictionaries and sets.
- Loops and automation.
- File operations.
- AWS automation using Boto3.
- Remote automation using Fabric.
- REST APIs and JSON.
- Flask API development.
- GitHub and JIRA integration.
- Python interview preparation.

---

# Next Step

The main goal is not just to learn Python syntax.

The real goal is to use Python for DevOps tasks such as:

- Automating repetitive tasks.
- Managing cloud infrastructure.
- Working with AWS APIs.
- Processing logs and files.
- Integrating DevOps tools.
- Building automation scripts.

## 🚀 Python for DevOps Journey - In Progress!
