from pydantic import BaseModel, Field
from typing import Optional

class RootInput(BaseModel):
    expression: str = Field(..., description="Expression involving roots to process")

class RewriteRootInput(RootInput):
    target: str = Field(..., description="Target form: 'pow' or 'sqrt'")

class NthRootInput(BaseModel):
    expression: str = Field(..., description="Expression to simplify")
    degree: int = Field(..., gt=1, description="Root degree (e.g. 2 for sqrt, 3 for cube root)")

class RootResult(BaseModel):
    result: str
    latex: str
