from pydantic import BaseModel, Field
from typing import List, Tuple

class PolyInput(BaseModel):
    expression: str = Field(..., description="Polynomial expression")
    variable: str = Field(default="x", description="Variable used in the expression")
    show_steps: bool = Field(default=False, description="Whether to show detailed steps")


class EvalInput(PolyInput):
    value: float = Field(..., description="Value to substitute for evaluation")

class DivideInput(BaseModel):
    dividend: str
    divisor: str
    variable: str = Field(default="x", description="Variable used in the polynomials")

class DegreeResult(BaseModel):
    degree: int

class CoefficientsResult(BaseModel):
    coefficients: List[str]

class EvalResult(BaseModel):
    value: float

class RootsResult(BaseModel):
    roots: List[str]

class ExpressionResult(BaseModel):
    result: str

class DivisionResult(BaseModel):
    quotient: str
    remainder: str


class FactorResult(BaseModel):
    result: str
    steps: List[str] = Field(default_factory=list)


class BinaryPolyInput(BaseModel):
    f: str
    g: str
    variable: str = Field(default="x", description="Variable used in the polynomials")

class ComposeInput(BaseModel):
    outer: str
    inner: str
    variable: str = Field(default="x", description="Variable used in both polynomials")

class CalcInput(BaseModel):
    expression: str
    variable: str = Field(default="x")
    show_steps: bool = Field(default=False)
