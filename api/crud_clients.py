from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from . import models, schemas


def get_client_by_name(db: Session, full_name: str):
    return db.query(models.Client).filter(models.Client.full_name == full_name).first()


def get_client_by_id(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientBase):
    db_client = models.Client(full_name=client.full_name, email=client.email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def disable_client(db: Session, client_id: int):
    try: 
        client = db.query(models.Client).filter(models.Client.id == client_id).one()
        client.is_active = False
        db.commit()
        db.refresh(client)
        return client
    except NoResultFound:
        db.rollback()
        return None


def delete_client(
        db: Session,
        client_id: int
):
    try:
        client = db.query(models.Client).filter(models.Client.id == client_id).one()
        db.delete(client)
        db.commit()
        return{"detail": "User successfully deleted"}
    except NoResultFound:
        db.rollback()
        return {"detail": "client not found"}
    



