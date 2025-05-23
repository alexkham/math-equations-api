from fastapi import APIRouter, HTTPException
from app.services import polynomials
from app.models.poly_schemas import (
    PolyInput, EvalInput, DivideInput,
    DegreeResult, CoefficientsResult, EvalResult,
    RootsResult, ExpressionResult, DivisionResult,FactorResult,BinaryPolyInput, ComposeInput, CalcInput
)
from app.models.poly_schemas import FactorResult  # noqa: F401



router = APIRouter(prefix="/polynomials", tags=["polynomials"])

@router.post("/degree", response_model=DegreeResult)
def get_degree(data: PolyInput):
    try:
        deg = polynomials.degree_poly(data.expression, data.variable)
        return {"degree": deg}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/coefficients", response_model=CoefficientsResult)
def get_coeffs(data: PolyInput):
    try:
        coeffs = polynomials.coefficients_poly(data.expression, data.variable)
        return {"coefficients": coeffs}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/evaluate", response_model=EvalResult)
def evaluate(data: EvalInput):
    try:
        val = polynomials.evaluate_poly(data.expression, data.variable, data.value)
        return {"value": val}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/roots", response_model=RootsResult)
def get_roots(data: PolyInput):
    try:
        rts = polynomials.roots_poly(data.expression, data.variable)
        return {"roots": rts}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/expand", response_model=ExpressionResult)
def expand(data: PolyInput):
    try:
        result = polynomials.expand_poly(data.expression)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# @router.post("/factor", response_model=ExpressionResult)
# def factor(data: PolyInput):
#     try:
#         result = polynomials.factor_poly(data.expression)
#         return {"result": result}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


@router.post("/factor", response_model=FactorResult)
def factor(data: PolyInput):
    try:
        if data.show_steps:
            result, steps = polynomials.factor_poly_steps(data.expression)
            return {"result": result, "steps": steps}
        else:
            result = polynomials.factor_poly(data.expression)
            return {"result": result, "steps": []}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/divide", response_model=DivisionResult)
def divide(data: DivideInput):
    try:
        quotient, remainder = polynomials.divide_polys(data.dividend, data.divisor, data.variable)
        return {"quotient": quotient, "remainder": remainder}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.post("/gcd", response_model=ExpressionResult)
def gcd_endpoint(data: BinaryPolyInput):
    try:
        result = polynomials.gcd_poly(data.f, data.g, data.variable)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/lcm", response_model=ExpressionResult)
def lcm_endpoint(data: BinaryPolyInput):
    try:
        result = polynomials.lcm_poly(data.f, data.g, data.variable)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/compose", response_model=ExpressionResult)
def compose_endpoint(data: ComposeInput):
    try:
        result = polynomials.compose_poly(data.outer, data.inner, data.variable)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/derive", response_model=ExpressionResult)
def derive_endpoint(data: CalcInput):
    try:
        result = polynomials.derive_poly(data.expression, data.variable)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/integrate", response_model=ExpressionResult)
def integrate_endpoint(data: CalcInput):
    try:
        result = polynomials.integrate_poly(data.expression, data.variable)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
