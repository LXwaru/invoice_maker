from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_users, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/users/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate, 
    db: Session = Depends(utils_db.get_db)
):
    db_user = crud_users.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud_users.create_user(db=db, user=user)


@router.get("/api/users/", response_model=list[schemas.User])
def list_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(utils_db.get_db)
):
    users = crud_users.get_users(db, skip=skip, limit=limit)
    return users