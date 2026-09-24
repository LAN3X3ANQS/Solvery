# Solvery

Solvery is an experimental algebra learning tool.

Instead of simply giving students the answer, Solvery checks their algebraic steps as they work toward it.

## Current Prototype

- Tokenizes algebraic expressions
- Parses equations
- Validates linear-equation transformations
- Detects some common mistakes
- Provides basic feedback
- Runs entirely in the terminal

## Example

```text
================================
          SOLVERY
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

## Run It

From the project directory:

```bash
python main.py
```

Enter `exit` to leave before reaching a final answer.

## Tests

```bash
python -m unittest discover -s tests
```

## Current Limitation

The prototype currently focuses on basic linear equations. Non-linear expressions such as `x^2` are not yet supported.

## Status

Solvery v0.1 / prototype.

Future milestones may include tablet handwriting input, real-time recognition, better mistake detection, and Ollama-powered tutoring.
