from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_employees, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/employees/", response_model=schemas.Employee)
def create_employee(
    employee: schemas.EmployeeBase, 
    db: Session = Depends(utils_db.get_db)
):
    db_employee = crud_employees.get_employee_by_name(db, full_name=employee.full_name)
    if db_employee:
        raise HTTPException(status_code=400, detail="employee name already registered")
    return crud_employees.create_employee(db=db, employee=employee)


@router.get("/api/employee/{employee_id}/", response_model=schemas.Employee)
def get_employee(
    employee_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_employees.get_employee_by_id(db=db, employee_id=employee_id)


@router.get("/api/employees/", response_model=list[schemas.Employee])
def list_employees(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(utils_db.get_db)
):
    employees = crud_employees.get_employees(db, skip=skip, limit=limit)
    return employees


@router.put("/api/employee/{employee_id}/")
def disable_employee(
    employee_id: int,
    db: Session = Depends(utils_db.get_db)
):
    result = crud_employees.disable_employee(db, employee_id=employee_id)
    if not result:
        raise HTTPException(status_code=404, detail='employee not found')
    return {"detail": "employee disabled successfully"}


@router.delete("/api/employee/{employee_id}/")
def delete_employee(
    employee_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_employees.delete_employee(db, employee_id)