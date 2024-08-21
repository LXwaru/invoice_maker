from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_service_item, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/service_items/', response_model=schemas.ServiceItemOut)
def create_service_item(
    service_item: schemas.ServiceItemIn,
    db: Session = Depends(utils_db.get_db)
):
    return crud_service_item.create_service_item(db=db, service_item=service_item)


@router.get('/api/service_items/', response_model=list[schemas.ServiceItemOut])
def list_service_items(
        skip: int = 0, 
        limit: int = 100,
        db: Session = Depends(utils_db.get_db)
):
    service_items = crud_service_item.get_service_items(db, skip=skip, limit=limit)
    return service_items


@router.get('/api/service_item/{service_item_id}/', response_model=schemas.ServiceItemOut)
def get_service_item(
    service_item_id: int,
    db: Session = Depends(utils_db.get_db)
):
    service_item = crud_service_item.get_service_item_by_id(db=db, service_item_id=service_item_id)
    if service_item is None:
        raise HTTPException(status_code=404, detail="Service item not found")
    
    return service_item
    


@router.delete('/api/service_item/{item_id}/')
def delete_service_item(
    service_item_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_service_item.delete_service_item(db, service_item_id)