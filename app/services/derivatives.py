from sympy import symbols, diff, parse_expr,latex



def compute_derivative(expr_str: str, var: str) -> tuple[str, str]:
    expr = parse_expr(expr_str)
    symbol = symbols(var)
    result = diff(expr, symbol)
    return str(result), f"$ {latex(result)} $"

def compute_higher_order(expr_str: str, var: str, order: int) -> tuple[str, str]:
    expr = parse_expr(expr_str)
    symbol = symbols(var)
    result = diff(expr, symbol, order)
    return str(result), f"$ {latex(result)} $"
