from fastapi import FastAPI, HTTPException, Body
from database.session import engine, SessionLocal, Base
from database.config import settings
from typing import List, Optional

import ReportOutput as ReportOutput
from Requests import Request
from Responses import Response

def create_tables():         
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    return app



app = start_application()

@app.post("/assignment/query")
async def read_report_paged(*, page: int , page_size: int, request: Request= Body(...)):
    if(page < 1 or page_size < 1):
        raise HTTPException(status_code=400, detail="Invalid page or page_size")
    
    reports = list(ReportOutput.get_page(SessionLocal(), page, page_size, request))

    results_dict = [dict(row.__dict__) for row in reports]
    
    return[
        Response(page= page, page_size=page_size, count=len(results_dict), results=results_dict)
    ]

