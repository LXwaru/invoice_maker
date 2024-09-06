from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_companies, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/users/{admin_id}/company/", response_model=schemas.Company)
def create_company_for_user(
    admin_id: int, 
    company: schemas.CompanyCreate, 
    db: Session = Depends(utils_db.get_db)
):
    return crud_companies.create_user_company(db=db, company=company, admin_id=admin_id)


@router.get("/api/users/{admin_id}/company/", response_model=list[schemas.Company])
def read_companies_by_admin_id(
    admin_id: int,
    db: Session = Depends(utils_db.get_db)
):
    company = crud_companies.get_company_by_admin_id(db=db, admin_id=admin_id)
    return company