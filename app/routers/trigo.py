from fastapi import APIRouter, HTTPException
from app.models.trigo_schemas import TrigInput, TrigRewriteInput, TrigResult, TrigEvalResult
from app.services import trigo

router = APIRouter(prefix="/trigo", tags=["trigonometry"])

@router.post("/simplify", response_model=TrigResult)
def simplify_trig_route(data: TrigInput):
    try:
        result, latex = trigo.simplify_trig(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/expand", response_model=TrigResult)
def expand_trig_route(data: TrigInput):
    try:
        result, latex = trigo.expand_trig_expr(data.expression)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rewrite", response_model=TrigResult)
def rewrite_trig_route(data: TrigRewriteInput):
    try:
        result, latex = trigo.rewrite_trig_expr(data.expression, data.target)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/evaluate", response_model=TrigEvalResult)
def eval_trig_route(data: TrigInput):
    try:
        value = trigo.eval_trig_expr(data.expression)
        return {"value": value}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
