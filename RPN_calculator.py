import re
from collections import deque
from typing import Union
import math

# Advanced Reverse Polish Notation Calculator

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

                n_numbers_needed = operator_function.__code__.co_argcount
                numbers_reversed_order = []
                for n in range(n_numbers_needed):
                    numbers_reversed_order.append(results_deque.pop())

                numbers = numbers_reversed_order[::-1]

                intermediate_res = operator_function(*numbers)

                results_deque.append(intermediate_res)

        final_res = results_deque.pop()
        return final_res

    print("""
Please write an arithmetic expression in RPN notation
Input example:
3.12 4 + 2 *
    """)

    rpn_expr_str = input()

    print(calculate_rpn(rpn_expr_str))


if __name__ == '__main__':
    main()
