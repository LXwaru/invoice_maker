from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_clients, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/clients/", response_model=schemas.Client)
def create_client(
    client: schemas.ClientBase, 
    db: Session = Depends(utils_db.get_db)
):
    db_client = crud_clients.get_client_by_name(db, full_name=client.full_name)
    if db_client:
        raise HTTPException(status_code=400, detail="client name already registered")
    return crud_clients.create_client(db=db, client=client)


@router.get("/api/client/{client_id}/", response_model=schemas.Client)
def get_client(
    client_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_clients.get_client_by_id(db=db, client_id=client_id)

@router.get("/api/clients/", response_model=list[schemas.Client])
def list_clients(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(utils_db.get_db)
):
    clients = crud_clients.get_clients(db, skip=skip, limit=limit)
    return clients

@router.put("/api/client/{client_id}/")
def disable_client(
    client_id: int,
    db: Session = Depends(utils_db.get_db)
):
    result = crud_clients.disable_client(db, client_id=client_id)
    if not result:
        raise HTTPException(status_code=404, detail='client not found')
    return {"detail": "client disabled successfully"}

@router.delete("/api/client/{client_id}/")
def delete_client(
    client_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_clients.delete_client(db, client_id)