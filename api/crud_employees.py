from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from . import models, schemas


def get_employee_by_name(db: Session, full_name: str):
    return db.query(models.Employee).filter(models.Employee.full_name == full_name).first()


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: schemas.EmployeeBase):
    db_employee = models.Employee(full_name=employee.full_name, email=employee.email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def disable_employee(db: Session, employee_id: int):
    try: 
        employee = db.query(models.Employee).filter(models.Employee.id == employee_id).one()
        employee.is_active = False
        db.commit()
        db.refresh(employee)
        return employee
    except NoResultFound:
        db.rollback()
        return None
    

def delete_employee(
        db: Session,
        employee_id: int
):
    try:
        employee = db.query(models.Employee).filter(models.Employee.id == employee_id).one()
        db.delete(employee)
        db.commit()
        return{"detail": "User successfully deleted"}
    except NoResultFound:
        db.rollback()
        return {"detail": "employee not found"}