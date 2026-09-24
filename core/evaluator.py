from core.parser import parse_expression


def evaluate(node, variables):
    node_type = node["type"]

    # Number
    if node_type == "NUMBER":
        return int(node["value"])

    # Variable
    if node_type == "VARIABLE":
        variable = node["value"]

        if variable not in variables:
            raise ValueError(f"No value was provided for {variable}.")

        return variables[variable]

    # Operation
    if node_type == "OPERATION":
        operator = node["operator"]

        left = evaluate(node["left"], variables)
        right = evaluate(node["right"], variables)

        if operator == "+":
            return left + right

        if operator == "-":
            return left - right

        if operator == "*":
            return left * right

        if operator == "/":
            return left / right

        raise ValueError(f"Unknown operator: {operator}")

    raise ValueError(f"Unknown node type: {node_type}")


# Temporary testing area

if __name__ == "__main__":
    expression = input("Enter an expression: ")

    tree = parse_expression(expression)

    variables = {}

    if "x" in expression:
        variables["x"] = float(input("Enter a value for x: "))

    result = evaluate(tree, variables)

    print("Result:", result)