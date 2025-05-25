from pydantic import BaseModel, Field
from typing import Optional

class ExponentInput(BaseModel):
    expression: str = Field(..., description="The expression to process")
    variable: Optional[str] = Field(default="x", description="Main symbol (if needed)")
    target: Optional[str] = Field(default=None, description="Target form to rewrite to (e.g. 'exp', 'log')")

class ExponentResult(BaseModel):
    result: str
    latex: str
