# Solvery Algebra Checker

Solvery Algebra Checker is an experimental algebra learning tool designed to help students **work through mathematics instead of simply receiving the answer**.

The current prototype focuses on checking a student's algebraic steps as they solve a linear equation. Rather than solving the problem for the student, Solvery evaluates each submitted step, identifies invalid transformations, and provides basic feedback.

## Current Prototype

The current version can:

* Tokenize algebraic expressions
* Parse equations
* Compare algebraic states between steps
* Validate transformations in basic linear equations
* Detect some common mistakes
* Provide basic hints and feedback
* Run entirely in the terminal

## Example

```text
================================
             SOLVERY ALGEBRA CHECKER
================================

Don't just get the answer.
Learn how to get there.

Enter your algebra problem: 2x + 5 = 15

Problem: 2x + 5 = 15

Your step: 2x = 15

Invalid step.

Hint: Check the operation you performed on the equation.

Try again.

Your step: 2x = 15 - 5

Valid step.

Your step: 2x / 2 = 10 / 2

Valid step.

Your step: x = 5

Valid step.

Final answer reached.
```

## How It Works

At a high level, Solvery follows the student's solution trajectory rather than immediately calculating the final answer.

```text
Student's Step
      ↓
Tokenization
      ↓
Parsing
      ↓
Mathematical Representation
      ↓
Step Verification
      ↓
Feedback
      ↓
Next Step
```

This is an early prototype of a larger idea: **understanding how a student arrived at an answer, not just whether the answer is correct.**

## Running Solvery

Clone the repository and navigate to the project directory.

Run the program:

```bash
python main.py
```

Enter `exit` to leave before reaching a final answer.

## Running Tests

The project includes automated tests for the mathematical components.

```bash
python -m unittest discover -s tests
```

## Current Limitations

This is an early prototype and currently has a limited mathematical scope.

* Primarily supports basic linear equations
* Non-linear expressions such as `x^2` are not currently supported
* Mistake detection is still limited
* Feedback is rule-based and relatively simple
* Input is currently text-based
* The interface runs entirely in the terminal

## Roadmap

Possible future directions include:

* More robust algebraic parsing
* Support for more mathematical operations
* Better detection of common misconceptions
* More detailed step-by-step feedback
* Tablet and handwriting input
* Mathematical expression recognition
* A graphical/web interface
* Student progress and learning history
* More adaptive tutoring
* Integration with local or hosted language models

## Project Status

**Solvery v0.1 — Experimental Prototype**

The current repository is primarily a **proof of concept for step-by-step algebra verification**.

The long-term vision for Solvery goes beyond this prototype: an educational system that can understand a student's mathematical input, track their solution process, identify where their reasoning goes wrong, and provide guidance without simply doing the mathematics for them.

For now, this repository represents the beginning of that idea.
