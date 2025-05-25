from sympy import symbols, Poly, simplify, sympify, div, roots, gcd, lcm
from sympy.parsing.sympy_parser import parse_expr
from typing import List, Tuple
from sympy import factor_list 

def get_symbol(var: str):
    return symbols(var)

def degree_poly(expr_str: str, var: str) -> int:
    expr = parse_expr(expr_str)
    poly = Poly(expr, get_symbol(var))
    return poly.degree()

def coefficients_poly(expr_str: str, var: str) -> List[str]:
    expr = parse_expr(expr_str)
    poly = Poly(expr, get_symbol(var))
    return [str(c) for c in poly.all_coeffs()]

def evaluate_poly(expr_str: str, var: str, value: float) -> float:
    expr = parse_expr(expr_str)
    symbol = get_symbol(var)
    substituted = expr.subs(symbol, value)
    return float(substituted.evalf())

def roots_poly(expr_str: str, var: str) -> List[str]:
    expr = parse_expr(expr_str)
    poly = Poly(expr, get_symbol(var))
    rts = roots(poly, multiple=True)
    return [str(r) for r in rts]

def expand_poly(expr_str: str) -> str:
    expr = parse_expr(expr_str)
    return str(simplify(expr.expand()))

def factor_poly(expr_str: str) -> str:
    expr = parse_expr(expr_str)
    return str(expr.factor())

def divide_polys(dividend_str: str, divisor_str: str, var: str) -> Tuple[str, str]:
    symbol = get_symbol(var)
    dividend = Poly(parse_expr(dividend_str), symbol)
    divisor = Poly(parse_expr(divisor_str), symbol)
    q, r = div(dividend, divisor, domain='QQ')
    return str(q.as_expr()), str(r.as_expr())




def factor_poly_steps(expr_str: str) -> Tuple[str, List[str]]:
    expr = parse_expr(expr_str)
    factored_expr = expr.factor()
    base, factors = factor_list(expr)

    steps = []
    if base != 1:
        steps.append(f"Constant factor: {base}")
    for factor, power in factors:
        if power == 1:
            steps.append(f"Factor: ({factor})")
        else:
            steps.append(f"Factor: ({factor})^{power}")

    return str(factored_expr), steps




def gcd_poly(f_str: str, g_str: str, var: str) -> str:
    symbol = symbols(var)
    f = Poly(parse_expr(f_str), symbol)
    g = Poly(parse_expr(g_str), symbol)
    return str(gcd(f, g).as_expr())

def lcm_poly(f_str: str, g_str: str, var: str) -> str:
    symbol = symbols(var)
    f = Poly(parse_expr(f_str), symbol)
    g = Poly(parse_expr(g_str), symbol)
    return str(lcm(f, g).as_expr())

def compose_poly(outer_str: str, inner_str: str, var: str) -> str:
    symbol = symbols(var)
    outer = Poly(parse_expr(outer_str), symbol)
    inner = Poly(parse_expr(inner_str), symbol)
    composed = outer.compose(inner)
    return str(composed.as_expr())

def derive_poly(expr_str: str, var: str) -> str:
    symbol = symbols(var)
    poly = Poly(parse_expr(expr_str), symbol)
    return str(poly.diff().as_expr())

def integrate_poly(expr_str: str, var: str) -> str:
    symbol = symbols(var)
    poly = Poly(parse_expr(expr_str), symbol)
    return str(poly.integrate().as_expr())
