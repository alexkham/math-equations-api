from fastapi import APIRouter, HTTPException
from app.models.schemas import ExpressionInput, ExpressionResult
from app.services import equations

router = APIRouter()

@router.post("/simplify", response_model=ExpressionResult)
def simplify_expr(data: ExpressionInput):
    try:
        result = equations.simplify_expr(data.expression)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/expand", response_model=ExpressionResult)
def expand_expr(data: ExpressionInput):
    try:
        result = equations.expand_expr(data.expression)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/factor", response_model=ExpressionResult)
def factor_expr(data: ExpressionInput):
    try:
        result = equations.factor_expr(data.expression)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/solve", response_model=ExpressionResult)
def solve_expr(data: ExpressionInput):
    try:
        result = equations.solve_equation(data.expression, data.variable)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/derive", response_model=ExpressionResult)
def derive_expr(data: ExpressionInput):
    try:
        result = equations.derive_expr(data.expression, data.variable)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/integrate", response_model=ExpressionResult)
def integrate_expr(data: ExpressionInput):
    try:
        result = equations.integrate_expr(data.expression, data.variable)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
