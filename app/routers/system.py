from fastapi import APIRouter, HTTPException
from app.models.system_schemas import SystemRequest, SystemResult
from app.services import system

router = APIRouter()

@router.post("/system", response_model=SystemResult)
def handle_system(data: SystemRequest):
    try:
        if data.operation == "solve":
            result = system.solve_system(data.equations, data.variables)
        elif data.operation == "simplify":
            result = system.simplify_system(data.equations, data.variables)
        elif data.operation == "rank":
            result = system.rank_system(data.equations, data.variables)
        else:
            raise ValueError("Unsupported operation.")
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
