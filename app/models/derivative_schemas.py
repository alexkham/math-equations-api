from pydantic import BaseModel, Field
from typing import Optional

class DerivativeInput(BaseModel):
    expression: str = Field(..., description="Expression to differentiate")
    variable: str = Field(default="x", description="Variable to differentiate by")

class HigherOrderInput(DerivativeInput):
    order: int = Field(..., gt=0, description="Order of the derivative")

class DerivativeResult(BaseModel):
    result: str
    latex: str

