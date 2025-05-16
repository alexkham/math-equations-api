from sympy import symbols, simplify, expand, factor, solve, diff, integrate
from sympy.parsing.sympy_parser import parse_expr
from typing import List, Union

def _get_symbol(var_name: str = "x"):
    return symbols(var_name)

def simplify_expr(expr_str: str) -> str:
    expr = parse_expr(expr_str)
    simplified = simplify(expr)
    return str(simplified)

def expand_expr(expr_str: str) -> str:
    expr = parse_expr(expr_str)
    expanded = expand(expr)
    return str(expanded)

def factor_expr(expr_str: str) -> str:
    expr = parse_expr(expr_str)
    factored = factor(expr)
    return str(factored)

def solve_equation(expr_str: str, var: str) -> List[str]:
    expr = parse_expr(expr_str)
    symbol = _get_symbol(var)
    solutions = solve(expr, symbol)
    return [str(s) for s in solutions]

def derive_expr(expr_str: str, var: str) -> str:
    expr = parse_expr(expr_str)
    symbol = _get_symbol(var)
    derivative = diff(expr, symbol)
    return str(derivative)

def integrate_expr(expr_str: str, var: str) -> str:
    expr = parse_expr(expr_str)
    symbol = _get_symbol(var)
    integral = integrate(expr, symbol)
    return str(integral)
