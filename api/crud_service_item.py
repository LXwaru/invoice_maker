from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from . import models, schemas


def create_service_item(
        db: Session,
        service_item: schemas.ServiceItemIn
):
    db_service_item = models.ServiceItem(
        teacher_id=service_item.teacher_id, 
        service_id=service_item.service_id
    )
    db.add(db_service_item)
    db.commit()
    db.refresh(db_service_item)
    return db_service_item


def get_service_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ServiceItem).offset(skip).limit(limit).all()


def get_service_item_by_id(db: Session, service_item_id: int):
    return db.query(models.ServiceItem).filter(models.ServiceItem.id == service_item_id).first()


def delete_service_item(
        db: Session,
        service_item_id: int
):
    try:
        service_item = db.query(models.ServiceItem).filter(models.ServiceItem.id == service_item_id).one()
        db.delete(service_item)
        db.commit()
        return{"detail": "Service item successfully deleted"}
    except NoResultFound:
        db.rollback()
        return {"detail": "Service item not found"}