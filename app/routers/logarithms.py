from fastapi import APIRouter, HTTPException
from app.models.logarithm_schemas import LogarithmInput, LogarithmResult
from app.services import logarithms

router = APIRouter(prefix="/logarithms", tags=["logarithms"])

@router.post("/simplify", response_model=LogarithmResult)
def simplify_route(data: LogarithmInput):
    """Simplify logarithmic expressions"""
    try:
        result, latex = logarithms.simplify_logarithm(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/expand", response_model=LogarithmResult)
def expand_route(data: LogarithmInput):
    """Expand logarithmic expressions using log properties"""
    try:
        result, latex = logarithms.expand_logarithm(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/combine", response_model=LogarithmResult)
def combine_route(data: LogarithmInput):
    """Combine logarithmic expressions into single logarithms"""
    try:
        result, latex = logarithms.combine_logarithm(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/factor", response_model=LogarithmResult)
def factor_route(data: LogarithmInput):
    """Factor logarithmic expressions"""
    try:
        result, latex = logarithms.factor_logarithm(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rewrite", response_model=LogarithmResult)
def rewrite_route(data: LogarithmInput):
    """Rewrite logarithmic expressions to different forms"""
    try:
        if not data.target:
            raise ValueError("Missing 'target' for rewrite.")
        result, latex = logarithms.rewrite_logarithm(data.expression, data.target)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/change-base", response_model=LogarithmResult)
def change_base_route(data: LogarithmInput):
    """Change the base of logarithmic expressions"""
    try:
        if not data.base:
            raise ValueError("Missing 'base' for base change.")
        result, latex = logarithms.change_base_logarithm(data.expression, data.base)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/solve", response_model=LogarithmResult)
def solve_route(data: LogarithmInput):
    """Solve logarithmic equations"""
    try:
        result, latex = logarithms.solve_logarithmic_equation(data.expression, data.variable)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/collect", response_model=LogarithmResult)
def collect_route(data: LogarithmInput):
    """Collect logarithmic terms with respect to a variable"""
    try:
        result, latex = logarithms.collect_logarithm(data.expression, data.variable)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rationalize", response_model=LogarithmResult)
def rationalize_route(data: LogarithmInput):
    """Rationalize logarithmic expressions"""
    try:
        result, latex = logarithms.rationalize_logarithm(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))