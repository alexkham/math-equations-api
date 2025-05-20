from fastapi import APIRouter, HTTPException
from app.models.logic_schemas import (
    LogicInput,
    LogicResult,
    TruthTableResult,
    SatisfiableInput,
    SatisfiableResult,
    AnalyzeLogicResult
)
from app.services import logic

router = APIRouter(prefix="/logic", tags=["logic"])


@router.post("/process", response_model=LogicResult)
def process_logic(data: LogicInput):
    """
    Transform a boolean logic expression into simplified, CNF, or DNF form.
    Returns both plain text and LaTeX versions.
    """
    try:
        result_str, result_latex = logic.process_logic_expression(data.expression, data.form)
        return {
            "result": result_str,
            "latex": result_latex
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/truth-table", response_model=TruthTableResult)
def truth_table_route(data: LogicInput):
    """
    Generate a full truth table for a given boolean expression.
    """
    try:
        variables, rows = logic.get_truth_table(data.expression)
        return {
            "variables": variables,
            "truth_table": rows
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/satisfiable", response_model=SatisfiableResult)
def satisfiable_route(data: SatisfiableInput):
    """
    Check if a boolean expression is satisfiable.
    If `full=true`, returns all satisfying assignments.
    """
    try:
        is_sat, models = logic.check_satisfiability(data.expression, data.full)
        return {
            "satisfiable": is_sat,
            "model": models
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# @router.post("/analyze", response_model=AnalyzeLogicResult)
# def analyze_route(data: LogicInput):
#     """
#     Perform full logic analysis:
#     - Simplify + LaTeX
#     - Satisfiability + sample model
#     - Tautology / Contradiction check
#     (Truth table is excluded)
#     """
#     try:
#         return logic.analyze_expression(data.expression)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))



@router.post("/analyze", response_model=AnalyzeLogicResult)
def analyze_route(data: LogicInput):
    """
    Perform full logic analysis:
    - Simplify + LaTeX
    - Satisfiability + model(s)
    - Tautology / Contradiction check
    (Truth table is excluded)
    """
    try:
        return logic.analyze_expression(data.expression, full=data.full)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
