from fastapi import APIRouter, HTTPException
from app.models.exponent_schemas import ExponentInput, ExponentResult
from app.services import exponents

router = APIRouter(prefix="/exponents", tags=["exponents"])

@router.post("/simplify", response_model=ExponentResult)
def simplify_route(data: ExponentInput):
    try:
        result, latex = exponents.simplify_exponent(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/expand", response_model=ExponentResult)
def expand_route(data: ExponentInput):
    try:
        result, latex = exponents.expand_exponent(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/factor", response_model=ExponentResult)
def factor_route(data: ExponentInput):
    try:
        result, latex = exponents.factor_exponent(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rewrite", response_model=ExponentResult)
def rewrite_route(data: ExponentInput):
    try:
        if not data.target:
            raise ValueError("Missing 'target' for rewrite.")
        result, latex = exponents.rewrite_exponent(data.expression, data.target)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
