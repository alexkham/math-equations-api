from sympy import Eq, solve
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols

x = symbols("x")  # Default single variable

def solve_equation(equation_str: str):
    if "=" not in equation_str:
        raise ValueError("Equation must contain '='.")

    left_str, right_str = equation_str.split("=")
    left_expr = parse_expr(left_str.strip())
    right_expr = parse_expr(right_str.strip())

    equation = Eq(left_expr, right_expr)
    result = solve(equation, x)

    return [str(r) for r in result]
