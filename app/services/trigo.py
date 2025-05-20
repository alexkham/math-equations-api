from sympy import symbols, sympify, simplify, trigsimp, expand_trig, latex
from sympy.parsing.sympy_parser import parse_expr, standard_transformations

def simplify_trig(expression: str) -> tuple[str, str]:
    expr = parse_expr(expression, transformations=standard_transformations)
    simplified = trigsimp(expr)
    return str(simplified), f"$ {latex(simplified)} $"

def expand_trig_expr(expression: str) -> tuple[str, str]:
    expr = parse_expr(expression, transformations=standard_transformations)
    expanded = expand_trig(expr)
    return str(expanded), f"$ {latex(expanded)} $"

# def rewrite_trig_expr(expression: str, target: str) -> tuple[str, str]:
#     expr = parse_expr(expression, transformations=standard_transformations)
#     rewritten = expr.rewrite(target)
#     return str(rewritten), f"$ {latex(rewritten)} $"


def rewrite_trig_expr(expression: str, target: str) -> tuple[str, str]:
    allowed_targets = {"exp", "sin", "cos", "tan", "cot", "log", "sqrt"}

    if target not in allowed_targets:
        raise ValueError(f"Unsupported rewrite target: '{target}'. Allowed: {', '.join(sorted(allowed_targets))}")

    expr = parse_expr(expression, transformations=standard_transformations)
    rewritten = expr.rewrite(target)

    if rewritten == expr:
        raise ValueError(f"The expression could not be rewritten to '{target}'.")

    return str(rewritten), f"$ {latex(rewritten)} $"


def eval_trig_expr(expression: str) -> float:
    expr = parse_expr(expression, transformations=standard_transformations)
    return float(expr.evalf())
