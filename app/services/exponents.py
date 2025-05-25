from sympy import simplify, expand, factor, symbols, latex
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformations = standard_transformations + (implicit_multiplication_application,)

def simplify_exponent(expr_str: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    result = simplify(expr)
    return str(result), f"${latex(result)}$"

def expand_exponent(expr_str: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    result = expand(expr, power_exp=True, log=False, multinomial=False)
    return str(result), f"${latex(result)}$"

def factor_exponent(expr_str: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations, evaluate=False)
    result = factor(expr)
    return str(result), f"${latex(result)}$"

# def rewrite_exponent(expr_str: str, target: str) -> tuple[str, str]:
#     expr = parse_expr(expr_str, transformations=transformations)
#     rewritten = expr.rewrite(target, evaluate=True)
#     return str(rewritten), f"${latex(rewritten)}$"


def rewrite_exponent(expr_str: str, target: str) -> tuple[str, str]:
    expr = parse_expr(expr_str, transformations=transformations)
    rewritten = expr.rewrite(target)
    result = simplify(rewritten)
    return str(result), f"${latex(result)}$"