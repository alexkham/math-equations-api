from pydantic import BaseModel, Field

class LaTeXInput(BaseModel):
    expression: str = Field(..., description="Math expression in LaTeX format")

class SymPyResult(BaseModel):
    result: str