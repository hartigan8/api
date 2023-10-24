from fastapi import FastAPI, HTTPException
from database.session import engine, SessionLocal, Base
from database.config import settings
from typing import List, Optional
from pydantic import BaseModel
import ReportOutput as ReportOutput

def create_tables():         
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    return app

class Filter(BaseModel):
    filters: dict
    ordering: Optional[List[dict]]

class Response(BaseModel):
    page: int
    page_size: int
    count: int
    results: List[dict]

app = start_application()

@app.post("/assignment/query")
async def read_report_paged(page: int, page_size: int):
    if(page < 1 or page_size < 1):
        raise HTTPException(status_code=400, detail="Invalid page or page_size")
    return ReportOutput.get_page(SessionLocal(), page, page_size)

