from fastapi import APIRouter, HTTPException
from app.models.latex_schemas import LaTeXInput, SymPyResult
from app.services.latex_converter import convert_latex_to_sympy

router = APIRouter(prefix="/latex", tags=["latex"])

@router.post("/convert", response_model=SymPyResult)
def convert_latex(input_data: LaTeXInput):
    """
    Convert LaTeX expression to SymPy format
    """
    try:
        result = convert_latex_to_sympy(input_data.expression)
        return SymPyResult(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")