from sympy import Implies, And, Or, Not, Equivalent, Symbol, latex
from sympy.logic.boolalg import simplify_logic, truth_table
from sympy.parsing.sympy_parser import parse_expr, standard_transformations
from sympy.core.sympify import SympifyError
from sympy.logic.inference import satisfiable

# Optional: import models if needed for typing in future
# from app.models.logic_schemas import AnalyzeLogicResult, SatisfiableResult, etc.

def process_logic_expression(expression: str, form: str = "raw") -> tuple[str, str]:
    try:
        local_dict = {
            "Implies": Implies,
            "And": And,
            "Or": Or,
            "Not": Not,
            "Equivalent": Equivalent
        }

        expr = parse_expr(
            expression,
            local_dict=local_dict,
            transformations=standard_transformations
        )

        expr = expr.rewrite(Implies).rewrite(Equivalent)

        if form == "cnf":
            transformed = simplify_logic(expr, form='cnf')
        elif form == "dnf":
            transformed = simplify_logic(expr, form='dnf')
        elif form == "simplify":
            transformed = simplify_logic(expr)
        else:
            transformed = expr

        return str(transformed), f"$$ {latex(transformed)} $$"

    except Exception as e:
        raise ValueError(f"Failed to process logic expression: {e}")


def get_truth_table(expression: str) -> tuple[list[str], list[dict]]:
    try:
        expr = parse_expr(expression, transformations=standard_transformations)
        variables = sorted(expr.free_symbols, key=lambda x: x.name)
        var_names = [str(v) for v in variables]
        table = []

        for row in truth_table(expr, variables):
            bools, result = row
            record = {str(var): bool(val) for var, val in zip(variables, bools)}
            record["result"] = bool(result)
            table.append(record)

        return var_names, table
    except Exception as e:
        raise ValueError(f"Failed to generate truth table: {e}")


def check_satisfiability(expression: str, full: bool = False) -> tuple[bool, list[dict] | None]:
    try:
        expr = parse_expr(expression, transformations=standard_transformations)
        result = satisfiable(expr, all_models=full)

        if not result:
            return False, None

        if full:
            return True, [{str(k): bool(v) for k, v in model.items()} for model in result]
        else:
            return True, [{str(k): bool(v) for k, v in result.items()}]

    except SympifyError:
        raise ValueError("Invalid logic expression")


# def analyze_expression(expression: str) -> dict:
#     try:
#         expr = parse_expr(expression, transformations=standard_transformations)
#         expr = expr.rewrite(Implies).rewrite(Equivalent)

#         simplified = simplify_logic(expr)
#         latex_str = f"$$ {latex(simplified)} $$"

#         # Check tautology/contradiction via truth table
#         variables = sorted(expr.free_symbols, key=lambda x: x.name)
#         all_true = True
#         all_false = True

#         for row in truth_table(expr, variables):
#             _, result = row
#             if result:
#                 all_false = False
#             else:
#                 all_true = False

#         # Satisfiability
#         sat_result = satisfiable(expr, all_models=False)
#         model = None
#         if sat_result:
#             model = [{str(k): bool(v) for k, v in sat_result.items()}]

#         return {
#             "result": str(simplified),
#             "latex": latex_str,
#             "is_tautology": all_true,
#             "is_contradiction": all_false,
#             "satisfiable": bool(sat_result),
#             "model": model
#         }

#     except Exception as e:
#         raise ValueError(f"Failed to analyze expression: {e}")



def analyze_expression(expression: str, full: bool = False) -> dict:

    expr = parse_expr(expression, transformations=standard_transformations)
    expr = expr.rewrite(Implies).rewrite(Equivalent)

    simplified = simplify_logic(expr)
    latex_str = f"$$ {latex(simplified)} $$"

    # Tautology / Contradiction
    variables = sorted(expr.free_symbols, key=lambda x: x.name)
    all_true = True
    all_false = True

    for row in truth_table(expr, variables):
        _, result = row
        if result:
            all_false = False
        else:
            all_true = False

    # Satisfiability
    sat_result = satisfiable(expr, all_models=full)
    model = None
    if sat_result:
        if full:
            model = [{str(k): bool(v) for k, v in m.items()} for m in sat_result]
        else:
            model = [{str(k): bool(v) for k, v in sat_result.items()}]

    return {
        "result": str(simplified),
        "latex": latex_str,
        "is_tautology": all_true,
        "is_contradiction": all_false,
        "satisfiable": bool(sat_result),
        "model": model
    }
