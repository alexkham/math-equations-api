from sympy import symbols, simplify, latex, root, sqrt, radsimp, expand, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = standard_transformations + (implicit_multiplication_application,)

def simplify_root(expr_str: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    result = simplify(expr)
    return str(result), f"${latex(result)}$"

def rationalize_root(expr_str: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    result = radsimp(expr)
    return str(result), f"${latex(result)}$"

def expand_root(expr_str: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    result = expand(expr, power_exp=False, mul=True, multinomial=True)
    return str(result), f"${latex(result)}$"

def combine_root(expr_str: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    result = simplify(expr)
    return str(result), f"${latex(result)}$"

def rewrite_root(expr_str: str, target: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    rewritten = expr.rewrite(target)
    return str(rewritten), f"${latex(rewritten)}$"

def nth_root(expr_str: str, degree: int) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    result = root(expr, degree)
    return str(result), f"${latex(result)}$"
