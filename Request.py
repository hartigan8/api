from typing import List, Optional, Union
from pydantic import BaseModel
class Filter(BaseModel):
    filters: dict
    ordering: Optional[List[dict]]