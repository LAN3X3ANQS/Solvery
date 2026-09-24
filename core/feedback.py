from core.parser import parse_expression


def get_terms(node, sign=1):
    if node["type"] == "NUMBER":
        return [(sign, node)]

    if node["type"] == "VARIABLE":
        return [(sign, node)]

    if node["type"] == "OPERATION":
        operator = node["operator"]

        if operator == "+":
            left_terms = get_terms(node["left"], sign)
            right_terms = get_terms(node["right"], sign)

            return left_terms + right_terms

        if operator == "-":
            left_terms = get_terms(node["left"], sign)
            right_terms = get_terms(node["right"], -sign)

            return left_terms + right_terms

    return [(sign, node)]


def get_equation_terms(equation):
    tree = parse_expression(equation)

    if tree["type"] != "EQUATION":
        raise ValueError("Expected an equation.")

    left_terms = get_terms(tree["left"])
    right_terms = get_terms(tree["right"])

    return left_terms, right_terms


def find_sign_error(previous, student):
    previous_left, previous_right = get_equation_terms(previous)
    student_left, student_right = get_equation_terms(student)

    previous_left_values = set(
        str(term) for sign, term in previous_left
    )

    previous_right_values = set(
        str(term) for sign, term in previous_right
    )

    student_left_values = set(
        str(term) for sign, term in student_left
    )

    student_right_values = set(
        str(term) for sign, term in student_right
    )

    # Look for a term that moved from left to right
    # while keeping the same sign.

    for previous_sign, previous_term in previous_left:
        term_text = str(previous_term)

        if (
            term_text in student_right_values
            and term_text not in student_left_values
        ):
            for student_sign, student_term in student_right:
                if str(student_term) == term_text:
                    if previous_sign == student_sign:
                        return True

    # Look for a term that moved from right to left
    # while keeping the same sign.

    for previous_sign, previous_term in previous_right:
        term_text = str(previous_term)

        if (
            term_text in student_left_values
            and term_text not in student_right_values
        ):
            for student_sign, student_term in student_left:
                if str(student_term) == term_text:
                    if previous_sign == student_sign:
                        return True

    return False


def one_side_operation(previous, student):
    previous_left, previous_right = get_equation_terms(previous)
    student_left, student_right = get_equation_terms(student)

    # If the right side stayed exactly the same,
    # but the left side changed, the student may
    # have performed an operation on only one side.

    if previous_right == student_right:
        if previous_left != student_left:
            return True

    # Same idea in the opposite direction.
    if previous_left == student_left:
        if previous_right != student_right:
            return True

    return False


if __name__ == "__main__":
    previous = input("Previous step: ")
    student = input("Student step: ")

    if find_sign_error(previous, student):
        print("Possible sign error detected.")

    elif one_side_operation(previous, student):
        print("Possible one-side operation detected.")

    else:
        print("No specific mistake detected.")