from pydantic import BaseModel, Field
from typing import Optional, List

class LogicInput(BaseModel):
    expression: str = Field(..., description="Boolean logic expression as a string")
    form: Optional[str] = Field(default="raw", description="Desired transformation: simplify, cnf, dnf")
    full: Optional[bool] = False  # 👈 this default is required


class LogicResult(BaseModel):
    result: str
    latex: str

class TruthTableResult(BaseModel):
    variables: List[str]
    truth_table: List[dict]

class SatisfiableInput(BaseModel):
    expression: str
    full: Optional[bool] = False  # return all satisfying assignments if true

class SatisfiableResult(BaseModel):
    satisfiable: bool
    model: Optional[List[dict]] = None  # list if full=True, single if full=False


class AnalyzeLogicResult(BaseModel):
    result: str
    latex: str
    is_tautology: bool
    is_contradiction: bool
    satisfiable: bool
    model: Optional[List[dict]]