# TestForge 🔧

An AI-powered test generation tool that automatically writes, reviews,
and runs test suites for Java and Python codebases.

---

## What it does

TestForge reads your source code, sends each function to an AI model
(Claude), generates pytest or JUnit 5 test suites, routes every test
through a mandatory human review stage, and automatically runs them
via a GitHub Actions CI pipeline on every commit.

---

## Features

- **Python + Java support** — parses both `.py` and `.java` files
- **AI test generation** — generates pytest and JUnit 5 test suites
- **Human review stage** — every AI-generated test requires approval
- **Auto-retry** — rejected tests are rewritten based on your feedback
- **SQLite audit log** — every session is logged with timestamps
- **Acceptance rate report** — track AI prompt quality over time
- **CI/CD pipeline** — GitHub Actions runs all tests on every push
- **85% coverage threshold** — build fails if coverage drops below 85%

---

## Project Structure

```
testforge/
├── src/
│   ├── parser.py       # reads Python and Java source files
│   ├── generator.py    # generates pytest and JUnit 5 tests
│   ├── reviewer.py     # human review with auto-retry (3 attempts)
│   └── logger.py       # SQLite audit log + acceptance rate report
├── tests/              # generated test files land here
├── logs/               # SQLite database lives here
├── .github/
│   └── workflows/
│       └── test.yml    # GitHub Actions CI pipeline
├── main.py             # entry point
└── requirements.txt
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/EDevika/testforge.git
cd testforge
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file in the root folder:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

---

## Usage

### Generate tests for a Python file

```bash
python main.py src/calculator.py
```

### Generate tests for a Java file

```bash
python main.py src/Calculator.java
```

### View acceptance rate report

```bash
python main.py --report
```

### Run all tests locally

```bash
pytest tests/ -v
```

---

## How it works

```
Your code → Parser reads functions → AI generates tests
→ You review (yes / no / edit) → Auto-retry on rejection
→ Tests saved → GitHub Actions runs them automatically
→ SQLite logs everything → Report shows acceptance rate
```

### Example session

```
Reading: src/calculator.py
Found 2 function(s): ['add', 'divide']

Generating tests for → add()...

============================================================
  GENERATED TEST FOR: add
============================================================
import pytest
from src.calculator import add

class Test_Add:
    def test_add_normal(self):
        result = add(1, 2)
        assert result is not None
    ...
============================================================

Accept this test? (yes / no / edit): yes
Logged: add → ACCEPTED
Tests saved to → tests/test_calculator.py
Done!
```

---

## Acceptance Rate Report

```
============================================================
  TESTFORGE — ACCEPTANCE RATE REPORT
============================================================
  Total tests generated  : 12
  Accepted               : 11 ✅
  Rejected               : 1  ❌
  Edited before accept   : 0  ✏️
  Acceptance rate        : 91.7%
============================================================
  Prompt quality: GOOD 👍 — Minor improvements needed
============================================================
```

---

## CI/CD Pipeline

Every push to `main` triggers GitHub Actions which:

1. Sets up Python 3.11
2. Installs all dependencies
3. Runs the full test suite with pytest
4. Publishes a JaCoCo coverage report as an artifact
5. Fails the build if coverage drops below 85%

---

## Tech Stack

- **Python 3.8+** — core language
- **Java** — supported source language for test generation
- **Claude API** — AI test generation (Anthropic)
- **pytest + pytest-cov** — Python test runner and coverage
- **JUnit 5** — Java test framework
- **SQLite** — lightweight audit database
- **GitHub Actions** — CI/CD pipeline
- **python-dotenv** — environment variable management

---

## Built by

Devika Eagala — [github.com/EDevika](https://github.com/EDevika)