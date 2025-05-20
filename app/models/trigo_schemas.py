from pydantic import BaseModel, Field
from typing import Optional

class TrigInput(BaseModel):
    expression: str = Field(..., description="Trigonometric expression to process")

class TrigRewriteInput(TrigInput):
    target: str = Field(..., description="Target function to rewrite as (e.g. 'exp', 'cos')")

class TrigResult(BaseModel):
    result: str
    latex: str

class TrigEvalResult(BaseModel):
    value: float
