from pydantic import BaseModel
from typing import List, Optional
from database.session import Base
class Request(BaseModel):
    filters: dict
    ordering: Optional[List[dict]]