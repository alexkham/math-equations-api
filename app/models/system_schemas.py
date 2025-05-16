from pydantic import BaseModel
from typing import List, Literal, Union, Dict

class SystemRequest(BaseModel):
    operation: Literal["solve", "simplify", "rank"]
    equations: List[str]
    variables: List[str]

class SystemResult(BaseModel):
    result: Union[Dict[str, str], List[str], int]
