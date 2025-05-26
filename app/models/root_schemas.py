from pydantic import BaseModel, Field, validator
from typing import Optional

class RootInput(BaseModel):
    expression: str
    assume_positive: bool = False

class RewriteRootInput(RootInput):
    target: str = Field(..., description="Target form: 'pow' or 'sqrt'")
    
    @validator('target')
    def validate_target(cls, v):
        if v.lower() not in ['pow', 'sqrt']:
            raise ValueError("target must be 'pow' or 'sqrt'")
        return v.lower()

class NthRootInput(BaseModel):
    expression: str
    degree: int = Field(..., gt=1, description="Root degree")

class RootResult(BaseModel):
    result: str
    latex: str