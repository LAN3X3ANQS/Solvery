from core.checker import check_step, is_final_answer
from core.feedback import find_sign_error, one_side_operation


def main():
    print("================================")
    print("          SOLVERY")
    print("================================")
    print()
    print("Don't just get the answer.")
    print("Learn how to get there.")
    print()

    problem = input("Enter your algebra problem: ")

    print()
    print("Problem:", problem)
    print()

    previous = problem

    while True:
        step = input("Your step: ")

        if step.lower() == "exit":
            break

        try:
            if check_step(previous, step):
                print("Valid step.")
                previous = step

                if is_final_answer(step):
                    print("Final answer reached.")
                    break
            else:
                print("Invalid step.")

                if find_sign_error(previous, step):
                    print("Hint: Check the sign of the term you moved.")
                elif one_side_operation(previous, step):
                    print("Hint: Check the operation you performed on the equation.")
                else:
                    print("Hint: Check the operation you performed on the equation.")

                print("Try again.")

        except ValueError as error:
            print("Checker error:", error)

        print()


if __name__ == "__main__":
    main()