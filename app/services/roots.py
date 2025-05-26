# from sympy import (
#     symbols, simplify, root, latex, parse_expr, Pow, expand, sqrt, Mul
# )
# from sympy.simplify.radsimp import radsimp
# from sympy.parsing.sympy_parser import (
#     standard_transformations, implicit_multiplication_application
# )


# from sympy import (
#     symbols, simplify, root, latex, parse_expr, Pow, expand, sqrt, Mul, Rational
# )
# from sympy.simplify.radsimp import radsimp
# from sympy.parsing.sympy_parser import (
#     standard_transformations, implicit_multiplication_application
# )


from sympy import (
    symbols, simplify, root, latex, parse_expr, Pow, expand, sqrt, Mul, Rational
)
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application
)

transformations = standard_transformations + (implicit_multiplication_application,)


# def _parse(expr_str: str, assume_positive: bool = False, evaluate: bool = False):
#     local_dict = {}
#     if assume_positive:
#         local_dict.update({ch: symbols(ch, positive=True) for ch in 'abcdefghijklmnopqrstuvwxyz'})
#     else:
#         local_dict.update({ch: symbols(ch) for ch in 'abcdefghijklmnopqrstuvwxyz'})
#     return parse_expr(expr_str, transformations=transformations, evaluate=evaluate, local_dict=local_dict)

def _parse(expr_str: str, assume_positive: bool = False, evaluate: bool = False):
    local_dict = {}
    if assume_positive:
        local_dict.update({ch: symbols(ch, positive=True) for ch in 'abcdefghijklmnopqrstuvwxyz'})
    else:
        local_dict.update({ch: symbols(ch) for ch in 'abcdefghijklmnopqrstuvwxyz'})
    return parse_expr(expr_str, transformations=transformations, evaluate=evaluate, local_dict=local_dict)



def simplify_root(expr_str: str, assume_positive: bool) -> tuple[str, str]:
    expr = _parse(expr_str, assume_positive, evaluate=True)
    result = simplify(expr)
    return str(result), f"${latex(result)}$"


def rationalize_root(expr_str: str, assume_positive: bool) -> tuple[str, str]:
    expr = _parse(expr_str, assume_positive, evaluate=True)
    result = radsimp(expr)
    return str(result), f"${latex(result)}$"


def expand_root(expr_str: str, assume_positive: bool) -> tuple[str, str]:
    expr = _parse(expr_str, assume_positive, evaluate=True)
    result = expand(expr, power_exp=True, mul=True)
    return str(result), f"${latex(result)}$"


def combine_root(expr_str: str, assume_positive: bool) -> tuple[str, str]:
    expr = _parse(expr_str, assume_positive, evaluate=True)

    if isinstance(expr, Mul):
        root_bases = []
        other_factors = []
        for term in expr.args:
            if isinstance(term, Pow) and term.exp == 1/2:
                root_bases.append(term.base)
            else:
                other_factors.append(term)

        if root_bases:
            combined = sqrt(Mul(*root_bases))
            if other_factors:
                result = Mul(*other_factors) * combined
            else:
                result = combined
            return str(result), f"${latex(result)}$"

    return str(expr), f"${latex(expr)}$"


# def rewrite_root(expr_str: str, target: str, assume_positive: bool) -> tuple[str, str]:
#     expr = _parse(expr_str, assume_positive, evaluate=True)
#     result = expr.rewrite(target)
#     return str(result), f"${latex(result)}$"


# def rewrite_root(expr_str: str, target: str, assume_positive: bool) -> tuple[str, str]:
#     expr = _parse(expr_str, assume_positive, evaluate=True)
#     result = expr.rewrite(target)
#     return str(result), f"${latex(result)}$"

# def rewrite_root(expr_str: str, target: str, assume_positive: bool) -> tuple[str, str]:
#     from sympy import symbols
#     expr = _parse(expr_str, assume_positive, evaluate=True)
    
#     if target.lower() == "pow":
#         # Convert sqrt(x) to x^(1/2) using subs
#         x = symbols('x')
#         result = expr.subs(sqrt(x), x**(Rational(1,2)))
#         # For any variable, not just x
#         for sym in expr.free_symbols:
#             result = result.subs(sqrt(sym), sym**(Rational(1,2)))
#     elif target.lower() == "sqrt":
#         # Convert x^(1/2) to sqrt(x)
#         for sym in expr.free_symbols:
#             result = expr.subs(sym**(Rational(1,2)), sqrt(sym))
#     else:
#         raise ValueError(f"Invalid target '{target}'. Must be 'pow' or 'sqrt'")
    
#     return str(result), f"${latex(result)}$"

# def nth_root(expr_str: str, degree: int, assume_positive: bool) -> tuple[str, str]:
#     expr = _parse(expr_str, assume_positive, evaluate=True)
#     result = simplify(root(expr, degree))
#     return str(result), f"${latex(result)}$"


# def rewrite_root(expr_str: str, target: str, assume_positive: bool) -> tuple[str, str]:
#     expr = _parse(expr_str, assume_positive)
#     result = expr.rewrite(target)
#     return str(result), f"${latex(result)}$"


# def rewrite_root(expr_str: str, target: str, assume_positive: bool) -> tuple[str, str]:
    expr = _parse(expr_str, assume_positive, evaluate=True)

    # Manually rewrite
    if target.lower() == "pow":
        # convert sqrt(x) to x**(1/2)
        rewritten = expr.replace(
            lambda e: isinstance(e, Pow) and e.exp == Rational(1, 2),
            lambda e: Pow(e.base, Rational(1, 2))  # safe but idempotent
        )
    elif target.lower() == "sqrt":
        # convert x**(1/2) to sqrt(x)
        rewritten = expr.replace(
            lambda e: isinstance(e, Pow) and e.exp == Rational(1, 2),
            lambda e: sqrt(e.base)
        )
    else:
        raise ValueError(f"Invalid target '{target}'. Must be 'pow' or 'sqrt'")

    return str(rewritten), f"${latex(rewritten)}$"

def rewrite_root(expr_str: str, target: str, assume_positive: bool) -> tuple[str, str]:
    expr = _parse(expr_str, assume_positive, evaluate=True)

    if target.lower() == "pow":
        # Match all sqrt() and convert to Pow(..., 1/2)
        rewritten = expr.replace(
            lambda e: isinstance(e, sqrt.__class__),
            lambda e: Pow(e.args[0], Rational(1, 2))
        )
    elif target.lower() == "sqrt":
        # Match all Pow(..., 1/2) and convert to sqrt()
        rewritten = expr.replace(
            lambda e: isinstance(e, Pow) and e.exp == Rational(1, 2),
            lambda e: sqrt(e.base)
        )
    else:
        raise ValueError("target must be 'pow' or 'sqrt'")

    return str(rewritten), f"${latex(rewritten)}$"


def nth_root(expr_str: str, degree: int, assume_positive: bool) -> tuple[str, str]:
    expr = _parse(expr_str, assume_positive, evaluate=True)
    result = simplify(root(expr, degree))
    return str(result), f"${latex(result)}$"
