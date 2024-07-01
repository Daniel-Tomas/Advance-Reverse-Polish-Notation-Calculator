import math
import re
from collections import deque


# Reverse Polish Notation Calculator

def main():
    def calculate_rpn(rpn_expr_str: str) -> float:

        rpn_expr_list = rpn_expr_str.split()

        results_deque = deque()
        operators_to_function = {'+': lambda x, y: x + y,
                                 '-': lambda x, y: x - y,
                                 '*': lambda x, y: x * y,
                                 '/': lambda x, y: x / y,
                                 'sqrt': lambda x: math.sqrt(x),
                                 }

        for str_ in rpn_expr_list:
            if re.fullmatch(r'[\d.]+', str_):
                results_deque.append(float(str_))
                continue

            if str_ in operators_to_function:
                operator_function = operators_to_function[str_]
                n_numbers_needed_for_operation = operator_function.__code__.co_argcount

                numbers_reversed_order = [results_deque.pop() for _ in range(n_numbers_needed_for_operation)]
                numbers = numbers_reversed_order[::-1]

                intermediate_res = operator_function(*numbers)

                results_deque.append(intermediate_res)

        final_res = results_deque.pop()
        return final_res

    rpn_expr_str_input = input("""
Example:
    Input:
        3.12 4 + 2 * sqrt
    Output:
        3.7735
        
Please write, as input, an arithmetic expression in RPN notation
""")

    print(calculate_rpn(rpn_expr_str_input))


if __name__ == '__main__':
    main()
