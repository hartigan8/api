from typing import List, Optional, Union
from pydantic import BaseModel
class Response(BaseModel):
    page: int
    page_size: int
    count: int
    results: List[dict]