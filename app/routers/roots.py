from fastapi import APIRouter, HTTPException
from app.services import roots
from app.models.root_schemas import (
    RootInput, RewriteRootInput, NthRootInput, RootResult
)

router = APIRouter(prefix="/roots", tags=["roots"])

@router.post("/simplify", response_model=RootResult)
def simplify_root_route(data: RootInput):
    try:
        result, latex = roots.simplify_root(data.expression, data.assume_positive)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rationalize", response_model=RootResult)
def rationalize_root_route(data: RootInput):
    try:
        result, latex = roots.rationalize_root(data.expression, data.assume_positive)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/expand", response_model=RootResult)
def expand_root_route(data: RootInput):
    try:
        result, latex = roots.expand_root(data.expression, data.assume_positive)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/combine", response_model=RootResult)
def combine_root_route(data: RootInput):
    try:
        result, latex = roots.combine_root(data.expression, data.assume_positive)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rewrite", response_model=RootResult)
def rewrite_root_route(data: RewriteRootInput):
    try:
        result, latex = roots.rewrite_root(data.expression, data.target, data.assume_positive)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/nth_root", response_model=RootResult)
def nth_root_route(data: NthRootInput):
    try:
        result, latex = roots.nth_root(data.expression, data.degree, assume_positive=False)
        return {"result": result, "latex": latex}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
