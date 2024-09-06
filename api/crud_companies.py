from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from . import models, schemas


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_company(db: Session, company: schemas.CompanyCreate, admin_id: int):
    db_company = models.Company(**company.model_dump(), admin_id=admin_id)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def get_company_by_owner_id(
        db: Session, 
        admin_id: int
):
    return db.query(models.Company).filter(models.Company.admin_id == admin_id)