from core.parser import parse_expression
from core.evaluator import evaluate


def compare(expression1, expression2, variables):
    tree1 = parse_expression(expression1)
    tree2 = parse_expression(expression2)

    result1 = evaluate(tree1, variables)
    result2 = evaluate(tree2, variables)

    return result1 == result2


# Temporary testing area

if __name__ == "__main__":
    first = input("Enter first expression: ")
    second = input("Enter second expression: ")

    variables = {}

    if "x" in first or "x" in second:
        variables["x"] = float(input("Enter a value for x: "))

    if compare(first, second, variables):
        print("Equivalent")
    else:
        print("Not equivalent")