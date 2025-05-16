from sympy import symbols, Eq, Matrix, solve
from sympy.parsing.sympy_parser import parse_expr
from typing import List, Dict, Union

def parse_system(equations: List[str], variables: List[str]):
    syms = symbols(variables)
    eqs = []

    for eq_str in equations:
        if "=" not in eq_str:
            raise ValueError(f"Invalid equation format: '{eq_str}'")
        left, right = eq_str.split("=")
        eq = Eq(parse_expr(left.strip()), parse_expr(right.strip()))
        eqs.append(eq)

    return eqs, syms

def solve_system(equations: List[str], variables: List[str]) -> Dict[str, str]:
    eqs, syms = parse_system(equations, variables)
    result = solve(eqs, syms, dict=True)

    if isinstance(result, list) and len(result) > 0:
        return {str(k): str(v) for k, v in result[0].items()}

    return {var: "unsolved" for var in variables}

def simplify_system(equations: List[str], variables: List[str]) -> List[str]:
    eqs, syms = parse_system(equations, variables)
    rows = []

    for eq in eqs:
        row = [eq.lhs.coeff(var) for var in syms]
        row.append(eq.rhs)
        rows.append(row)

    matrix = Matrix(rows).rref()[0]
    return [str(list(row)) for row in matrix.tolist()]

def rank_system(equations: List[str], variables: List[str]) -> int:
    eqs, syms = parse_system(equations, variables)
    rows = []

    for eq in eqs:
        row = [eq.lhs.coeff(var) for var in syms]
        row.append(eq.rhs)
        rows.append(row)

    matrix = Matrix(rows)
    return matrix.rank()
