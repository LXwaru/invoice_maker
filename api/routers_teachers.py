from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud, utils_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/api/teachers", response_model=schemas.TeacherBase)
def create_teacher(
    teacher: schemas.TeacherBase, 
    db: Session = Depends(utils_db.get_db)):
    db_teacher = crud.get_teacher_by_name(db, full_name=teacher.full_name)
    if db_teacher:
        raise HTTPException(status_code=400, detail="teacher name already registered")
    return crud.create_teacher(db=db, teacher=teacher)