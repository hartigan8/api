from pydantic import BaseModel
from typing import List
class Response(BaseModel):
    page: int
    page_size: int
    count: int
    results: List[dict]
