import os
import sys


if __package__ is None or __package__ == "":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


from core.parser import parse_expression
from core.feedback import find_sign_error


def expression_to_linear(node):
    node_type = node["type"]

    # Number
    if node_type == "NUMBER":
        return 0, float(node["value"])

    # Variable
    if node_type == "VARIABLE":
        if node["value"] == "x":
            return 1, 0

        raise ValueError(f"Unsupported variable: {node['value']}")

    # Operation
    if node_type == "OPERATION":
        operator = node["operator"]

        left_x, left_constant = expression_to_linear(node["left"])
        right_x, right_constant = expression_to_linear(node["right"])

        if operator == "+":
            return (
                left_x + right_x,
                left_constant + right_constant
            )

        if operator == "-":
            return (
                left_x - right_x,
                left_constant - right_constant
            )

        if operator == "*":
            # x * x would create x², which we don't support yet
            if left_x != 0 and right_x != 0:
                raise ValueError("Non-linear expression.")

            if right_x == 0:
                return (
                    left_x * right_constant,
                    left_constant * right_constant
                )

            if left_x == 0:
                return (
                    right_x * left_constant,
                    right_constant * left_constant
                )

        if operator == "/":
            # Division by an expression containing x
            # would create a non-linear/rational expression.
            if right_x != 0:
                raise ValueError("Division by an expression containing x.")

            if right_constant == 0:
                raise ValueError("Division by zero.")

            return (
                left_x / right_constant,
                left_constant / right_constant
            )

        raise ValueError(f"Unsupported operator: {operator}")

    raise ValueError(f"Unknown node type: {node_type}")


def equation_to_linear(equation):
    tree = parse_expression(equation)

    if tree["type"] != "EQUATION":
        raise ValueError("Expected an equation.")

    left_x, left_constant = expression_to_linear(tree["left"])
    right_x, right_constant = expression_to_linear(tree["right"])

    # Move everything to the left:
    #
    # left = right
    #
    # becomes:
    #
    # ax + b = 0

    x_coefficient = left_x - right_x
    constant = left_constant - right_constant

    return x_coefficient, constant


def normalize_equation(equation):
    x_coefficient, constant = equation_to_linear(equation)

    # 0x + 0 = 0
    if x_coefficient == 0 and constant == 0:
        return 0, 0

    # 0x + b = 0
    if x_coefficient == 0:
        return 0, 1 if constant > 0 else -1

    # Normalize so that the x coefficient is 1
    constant = constant / x_coefficient

    return 1, constant


def check_step(previous, student):
    previous_normalized = normalize_equation(previous)
    student_normalized = normalize_equation(student)

    return previous_normalized == student_normalized


def is_final_answer(equation):
    tree = parse_expression(equation)

    if tree["type"] != "EQUATION":
        return False

    left = tree["left"]
    right = tree["right"]

    # x = something
    if (
        left["type"] == "VARIABLE"
        and left["value"] == "x"
    ):
        return True

    # something = x
    if (
        right["type"] == "VARIABLE"
        and right["value"] == "x"
    ):
        return True

    return False


if __name__ == "__main__":
    equation = input("Enter equation: ")

    if is_final_answer(equation):
        print("Final answer reached.")
    else:
        print("Not final yet.")