from pydantic import BaseModel, Field
from typing import Optional

class LogarithmInput(BaseModel):
    expression: str = Field(..., description="The logarithmic expression to process")
    variable: Optional[str] = Field(default="x", description="Main symbol (if needed)")
    target: Optional[str] = Field(default=None, description="Target form to rewrite to (e.g. 'exp', 'log')")
    base: Optional[str] = Field(default=None, description="Base for logarithm operations")

class LogarithmResult(BaseModel):
    result: str
    latex: str