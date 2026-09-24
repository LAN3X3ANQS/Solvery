from core.tokenizer import tokenize


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]

        return None

    def advance(self):
        self.position += 1

    def parse(self):
        left = self.parse_expression()

        token = self.current()

        if token and token[1] == "=":
            self.advance()

            right = self.parse_expression()

            return {
                "type": "EQUATION",
                "left": left,
                "right": right
            }

        return left

    def parse_expression(self):
        expression = self.parse_term()

        while self.current() and self.current()[1] in ("+", "-"):
            operator = self.current()[1]
            self.advance()

            right = self.parse_term()

            expression = {
                "type": "OPERATION",
                "operator": operator,
                "left": expression,
                "right": right
            }

        return expression

    def parse_term(self):
        expression = self.parse_factor()

        while self.current():
            token = self.current()

            if token[1] in ("*", "/"):
                operator = token[1]
                self.advance()

                right = self.parse_factor()

                expression = {
                    "type": "OPERATION",
                    "operator": operator,
                    "left": expression,
                    "right": right
                }

            elif self.can_multiply_implicitly():
                right = self.parse_factor()

                expression = {
                    "type": "OPERATION",
                    "operator": "*",
                    "left": expression,
                    "right": right
                }

            else:
                break

        return expression

    def parse_factor(self):
        token = self.current()

        if token is None:
            raise ValueError("Expected a value.")

        token_type, value = token

        # Number
        if token_type == "NUMBER":
            self.advance()

            return {
                "type": "NUMBER",
                "value": value
            }

        # Variable
        if token_type == "VARIABLE":
            self.advance()

            return {
                "type": "VARIABLE",
                "value": value
            }

        # Parentheses
        if token_type == "PARENTHESIS" and value == "(":
            self.advance()

            expression = self.parse_expression()

            token = self.current()

            if token is None or token[1] != ")":
                raise ValueError("Missing closing parenthesis.")

            self.advance()

            return expression

        raise ValueError(f"Unexpected token: {token}")

    def can_multiply_implicitly(self):
        token = self.current()

        if token is None:
            return False

        token_type, value = token

        return (
            token_type in ("NUMBER", "VARIABLE")
            or (token_type == "PARENTHESIS" and value == "(")
        )


def parse_expression(text):
    tokens = tokenize(text)

    parser = Parser(tokens)

    return parser.parse()


if __name__ == "__main__":
    expression = input("Enter an equation: ")

    try:
        result = parse_expression(expression)
        print(result)

    except ValueError as error:
        print("Parser error:", error)

