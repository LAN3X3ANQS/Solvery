def tokenize(expression):
    tokens = []
    i = 0

    while i < len(expression):
        char = expression[i]

        # Ignore spaces
        if char.isspace():
            i += 1
            continue

        # Number
        if char.isdigit():
            number = ""

            while i < len(expression) and expression[i].isdigit():
                number += expression[i]
                i += 1

            tokens.append(("NUMBER", number))
            continue

        # Variable
        if char.isalpha():
            tokens.append(("VARIABLE", char))
            i += 1
            continue

        # Operators
        if char in "+-*/=":
            tokens.append(("OPERATOR", char))
            i += 1
            continue

        # Parentheses
        if char in "()":
            tokens.append(("PARENTHESIS", char))
            i += 1
            continue

        # Unknown character
        tokens.append(("UNKNOWN", char))
        i += 1

    return tokens


if __name__ == "__main__":
    expression = input("Enter an expression: ")

    tokens = tokenize(expression)

    print(tokens)

