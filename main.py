from fastapi import FastAPI, HTTPException, status
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from session import engine 
from config import settings
from Request import Filter
from Response import Response

def create_tables():         
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    return app

Base = declarative_base()

class ReportOutputModel(Base):
    __tablename__ = "report_output"
    
    id = Column(Integer, primary_key=True, index=True)
    row = Column(Integer, nullable=True)
    main_uploaded_variation = Column(String, nullable=True)
    main_existing_variation = Column(String, nullable=True)
    main_symbol = Column(String, nullable=True)
    main_af_vcf = Column(String, nullable=True)
    main_dp = Column(Integer, nullable=True)
    details2_provean = Column(String, nullable=True)
    details2_dann_score = Column(Integer, nullable=True)
    links_mondo = Column(String, nullable=True)
    links_pheno_pubmed = Column(String, nullable=True)
    





app = start_application()

@app.post("/assignment/query")
async def read_report_output(page: int, page_size: int):
    if(page < 1 or page_size < 1 or page == None or page_size == None):
        raise HTTPException(status_code=400, detail="Invalid page or page_size")
    


