from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_teachers, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/teachers", response_model=schemas.Teacher)
def create_teacher(
    teacher: schemas.TeacherBase, 
    db: Session = Depends(utils_db.get_db)
):
    db_teacher = crud_teachers.get_teacher_by_name(db, full_name=teacher.full_name)
    if db_teacher:
        raise HTTPException(status_code=400, detail="teacher name already registered")
    return crud_teachers.create_teacher(db=db, teacher=teacher)


@router.get("/api/teacher/{teacher_id}", response_model=schemas.Teacher)
def get_teacher(
    teacher_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_teachers.get_teacher_by_id(db=db, teacher_id=teacher_id)

@router.get("/api/teachers", response_model=list[schemas.Teacher])
def list_teachers(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(utils_db.get_db)
):
    teachers = crud_teachers.get_teachers(db, skip=skip, limit=limit)
    return teachers

@router.delete("/api/teacher/{teacher_id}/")
def delete_teacher(
    teacher_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_teachers.delete_teacher(db, teacher_id)