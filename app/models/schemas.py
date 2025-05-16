from pydantic import BaseModel
from typing import Union, List

class ExpressionInput(BaseModel):
    expression: str
    variable: str = "x"

class ExpressionResult(BaseModel):
    result: Union[str, List[str]]
