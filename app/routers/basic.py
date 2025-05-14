from fastapi import APIRouter, HTTPException
from app.models.schemas import EquationInput, EquationResult
from app.services.basic import solve_equation

router = APIRouter()

@router.post("/solve", response_model=EquationResult)
def solve_math_equation(data: EquationInput):
    try:
        solutions = solve_equation(data.equation)
        return {"solutions": solutions}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid equation: {str(e)}")
