from sympy import (
    symbols,
    sympify,
    simplify,
    trigsimp,
    expand_trig,
    latex,
    diff,
    integrate,
    Symbol,
    together,
)
from sympy.parsing.sympy_parser import parse_expr, standard_transformations



def simplify_trig(expression: str) -> tuple[str, str]:
    """
    Simplify a trigonometric expression and format the result cleanly.
    """
    expr = parse_expr(expression, transformations=standard_transformations)
    simplified = trigsimp(expr)
    # Format as a proper fraction if applicable
    formatted = together(simplified)
    return str(formatted), f"$ {latex(formatted)} $"


def expand_trig_expr(expression: str) -> tuple[str, str]:
    """
    Expand trigonometric identities (e.g., sin(a + b)).
    """
    expr = parse_expr(expression, transformations=standard_transformations)
    expanded = expand_trig(expr)
    return str(expanded), f"$ {latex(expanded)} $"


def rewrite_trig_expr(expression: str, target: str) -> tuple[str, str]:
    """
    Rewrite a trig expression in terms of another function, if allowed.
    """
    allowed_targets = {"exp", "sin", "cos", "tan", "cot", "log", "sqrt"}

    if target not in allowed_targets:
        raise ValueError(
            f"Unsupported rewrite target: '{target}'. "
            f"Allowed: {', '.join(sorted(allowed_targets))}"
        )

    expr = parse_expr(expression, transformations=standard_transformations)
    rewritten = expr.rewrite(target)

    if rewritten == expr:
        raise ValueError(f"The expression could not be rewritten to '{target}'.")

    return str(rewritten), f"$ {latex(rewritten)} $"


def eval_trig_expr(expression: str) -> float:
    """
    Evaluate a trig expression numerically.
    """
    expr = parse_expr(expression, transformations=standard_transformations)
    return float(expr.evalf())


def derive_trig_expr(expression: str, variable: str) -> tuple[str, str]:
    """
    Differentiate a trig expression with respect to a variable.
    """
    expr = parse_expr(expression, transformations=standard_transformations)
    var = Symbol(variable)
    derivative = diff(expr, var)
    return str(derivative), f"$ {latex(derivative)} $"


def integrate_trig_expr(expression: str, variable: str) -> tuple[str, str]:
    """
    Integrate a trig expression with respect to a variable.
    """
    expr = parse_expr(expression, transformations=standard_transformations)
    var = Symbol(variable)
    integral = integrate(expr, var)
    return str(integral), f"$ {latex(integral)} $"
