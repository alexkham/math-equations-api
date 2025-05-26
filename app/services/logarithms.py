from sympy import (
    simplify, expand, factor, symbols, latex, log, ln, exp, 
    expand_log, logcombine, collect, cancel, together
)
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformations = standard_transformations + (implicit_multiplication_application,)

def simplify_logarithm(expr_str: str) -> tuple[str, str]:
    """Simplify logarithmic expressions"""
    expr = parse_expr(expr_str, transformations=transformations)
    result = simplify(expr)
    return str(result), f"${latex(result)}$"

def expand_logarithm(expr_str: str) -> tuple[str, str]:
    """Expand logarithmic expressions using log properties"""
    expr = parse_expr(expr_str, transformations=transformations)
    result = expand_log(expr, force=True)
    return str(result), f"${latex(result)}$"

def combine_logarithm(expr_str: str) -> tuple[str, str]:
    """Combine logarithmic expressions into single logarithms"""
    expr = parse_expr(expr_str, transformations=transformations)
    result = logcombine(expr, force=True)
    return str(result), f"${latex(result)}$"

def factor_logarithm(expr_str: str) -> tuple[str, str]:
    """Factor logarithmic expressions"""
    expr = parse_expr(expr_str, transformations=transformations, evaluate=False)
    result = factor(expr)
    return str(result), f"${latex(result)}$"

def rewrite_logarithm(expr_str: str, target: str) -> tuple[str, str]:
    """Rewrite logarithmic expressions to different forms"""
    expr = parse_expr(expr_str, transformations=transformations)
    
    # Handle different target types
    if target.lower() == 'exp':
        rewritten = expr.rewrite(exp)
    elif target.lower() in ['log', 'ln']:
        rewritten = expr.rewrite(log)
    else:
        # Try to parse target as a symbol
        target_symbol = parse_expr(target, transformations=transformations)
        rewritten = expr.rewrite(target_symbol)
    
    result = simplify(rewritten)
    return str(result), f"${latex(result)}$"

# def change_base_logarithm(expr_str: str, new_base: str) -> tuple[str, str]:
#     """Change the base of logarithmic expressions"""
#     expr = parse_expr(expr_str, transformations=transformations)
#     base_expr = parse_expr(new_base, transformations=transformations)
    
#     # Apply change of base formula: log_a(x) = log_b(x) / log_b(a)
#     result = expr.subs(log, lambda x, b=None: log(x, base_expr) if b is None else log(x, b))
#     result = simplify(result)
#     return str(result), f"${latex(result)}$"

# def change_base_logarithm(expr_str: str, new_base: str) -> tuple[str, str]:
#     """Change the base of logarithmic expressions"""
#     from sympy import log, simplify, symbols
    
#     expr = parse_expr(expr_str, transformations=transformations)
#     new_base_expr = parse_expr(new_base, transformations=transformations)
    
#     # Manual traversal to replace log functions
#     if expr.func == log:
#         if len(expr.args) == 2:
#             # log(x, base) -> log(x)/log(new_base)
#             x = expr.args[0]
#             result = log(x) / log(new_base_expr)
#         else:
#             # log(x) -> log(x)/log(new_base)  
#             x = expr.args[0]
#             result = log(x) / log(new_base_expr)
#     else:
#         result = expr
    
#     result = simplify(result)
#     return str(result), f"${latex(result)}$"

# def change_base_logarithm(expr_str: str, new_base: str) -> tuple[str, str]:
#     """Change the base of logarithmic expressions"""
#     expr = parse_expr(expr_str, transformations=transformations)
#     new_base_expr = parse_expr(new_base, transformations=transformations)
    
#     if expr.func == log:
#         # Get the argument (x)
#         x = expr.args[0]
#         # Always use change of base formula: log_oldbase(x) = log(x)/log(newbase)
#         result = log(x) / log(new_base_expr)
#     else:
#         result = expr
    
#     result = simplify(result)
#     return str(result), f"${latex(result)}$"

# def change_base_logarithm(expr_str: str, new_base: str) -> tuple[str, str]:
#     """Change the base of logarithmic expressions"""
#     print(f"DEBUG: new_base parameter = {new_base}")
    
#     expr = parse_expr(expr_str, transformations=transformations)
#     new_base_expr = parse_expr(new_base, transformations=transformations)
    
#     print(f"DEBUG: new_base_expr = {new_base_expr}")
#     print(f"DEBUG: type(new_base_expr) = {type(new_base_expr)}")
    
#     if expr.func == log:
#         x = expr.args[0]
#         result = log(x) / log(new_base_expr)
#         print(f"DEBUG: result before simplify = {result}")
#     else:
#         result = expr
    
#     result = simplify(result)
#     return str(result), f"${latex(result)}$"



def change_base_logarithm(expr_str: str, new_base: str) -> tuple[str, str]:
    """Change the base of logarithmic expressions"""
    expr = parse_expr(expr_str, transformations=transformations)
    new_base_expr = parse_expr(new_base, transformations=transformations)
    
    if expr.func == log and len(expr.args) == 2:
        x = expr.args[0]
        old_base = expr.args[1]
        # log_oldbase(x) = log_newbase(x) / log_newbase(oldbase)
        # So: log_newbase(x) = log_oldbase(x) * log_newbase(oldbase)
        result = expr * log(old_base, new_base_expr)
    else:
        result = expr
    
    result = simplify(result)
    return str(result), f"${latex(result)}$"

def solve_logarithmic_equation(expr_str: str, variable: str = "x") -> tuple[str, str]:
    """Solve logarithmic equations"""
    from sympy import solve, Eq
    
    # Check if it's an equation (contains =)
    if '=' in expr_str:
        left, right = expr_str.split('=', 1)
        left_expr = parse_expr(left.strip(), transformations=transformations)
        right_expr = parse_expr(right.strip(), transformations=transformations)
        equation = Eq(left_expr, right_expr)
    else:
        # Assume equation equals zero
        expr = parse_expr(expr_str, transformations=transformations)
        equation = Eq(expr, 0)
    
    var = symbols(variable)
    solutions = solve(equation, var)
    
    if not solutions:
        result = "No solution"
        latex_result = "\\text{No solution}"
    elif len(solutions) == 1:
        result = str(solutions[0])
        latex_result = latex(solutions[0])
    else:
        result = str(solutions)
        latex_result = latex(solutions)
    
    return result, f"${latex_result}$"

def collect_logarithm(expr_str: str, variable: str = "x") -> tuple[str, str]:
    """Collect logarithmic terms with respect to a variable"""
    expr = parse_expr(expr_str, transformations=transformations)
    var = symbols(variable)
    result = collect(expr, log(var))
    return str(result), f"${latex(result)}$"

def rationalize_logarithm(expr_str: str) -> tuple[str, str]:
    """Rationalize logarithmic expressions"""
    expr = parse_expr(expr_str, transformations=transformations)
    result = together(cancel(expr))
    return str(result), f"${latex(result)}$"