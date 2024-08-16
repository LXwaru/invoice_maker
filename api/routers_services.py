from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud_services, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/services/', response_model=schemas.ServiceOut)
def create_service(
    service: schemas.ServiceIn,
    db: Session = Depends(utils_db.get_db)
):
    db_service = crud_services.lookup_service_by_name(db, title=service.title)
    if db_service:
        raise HTTPException(status_code=400, detail="service already registered")
    return crud_services.register_new_service(db=db, service=service)

@router.get('/api/services/', response_model=list[schemas.ServiceOut])
def list_services(
        skip: int = 0, 
        limit: int = 100,
        db: Session = Depends(utils_db.get_db)
):
    services = crud_services.get_services(db, skip=skip, limit=limit)
    return services

@router.get('/api/service/{service_id}/', response_model=schemas.ServiceOut)
def get_service(
    service_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_services.get_services_by_id(db=db, service_id=service_id)


@router.delete("/api/service/{service_id}/")
def delete_service(
    service_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_services.delete_service(db, service_id)