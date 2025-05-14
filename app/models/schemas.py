from pydantic import BaseModel
from typing import List

class EquationInput(BaseModel):
    equation: str

class EquationResult(BaseModel):
    solutions: List[str]
