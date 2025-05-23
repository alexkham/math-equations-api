from fastapi import APIRouter, HTTPException
from app.services import derivatives
from app.models.derivative_schemas import DerivativeInput, HigherOrderInput, DerivativeResult

router = APIRouter(prefix="/derivatives", tags=["derivatives"])

# @router.post("/differentiate", response_model=DerivativeResult)
# def differentiate(data: DerivativeInput):
#     try:
#         result = derivatives.compute_derivative(data.expression, data.variable)
#         return {"result": result}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.post("/higher", response_model=DerivativeResult)
# def higher_order(data: HigherOrderInput):
#     try:
#         result = derivatives.compute_higher_order(data.expression, data.variable, data.order)
#         return {"result": result}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


@router.post("/differentiate", response_model=DerivativeResult)
def differentiate(data: DerivativeInput):
    try:
        result, latex_expr = derivatives.compute_derivative(data.expression, data.variable)
        return {"result": result, "latex": latex_expr}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/higher", response_model=DerivativeResult)
def higher_order(data: HigherOrderInput):
    try:
        result, latex_expr = derivatives.compute_higher_order(data.expression, data.variable, data.order)
        return {"result": result, "latex": latex_expr}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
