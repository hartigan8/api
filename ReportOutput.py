from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database.session import Base
from Requests import Request

class ReportOutput(Base):
    __tablename__ = "report_output"
    row = Column(Integer, primary_key=True, nullable=True)
    main_uploaded_variation = Column(String, nullable=True)
    main_existing_variation = Column(String, nullable=True)
    main_symbol = Column(String, nullable=True)
    main_af_vcf = Column(String, nullable=True)
    main_dp = Column(Integer, nullable=True)
    details2_provean = Column(String, nullable=True)
    details2_dann_score = Column(Integer, nullable=True)
    links_mondo = Column(String, nullable=True)
    links_pheno_pubmed = Column(String, nullable=True)

def get_page(db: Session, page: int, page_size: int, request: Request):
    
    filters = request.filters # dict
    order = request.ordering # List[dict]
    # TODO filtering
    q = db.query(ReportOutput)
    for attr, value in filters.items():
        q = q.filter(getattr(ReportOutput, attr).like("%%%s%%" % value))
    
    # TODO ordering



    return q.all()

