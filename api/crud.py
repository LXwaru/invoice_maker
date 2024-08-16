from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from . import models, schemas


# def get_teacher(db: Session, teacher_id: int):
#     return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()


def get_teacher_by_name(db: Session, full_name: str):
    return db.query(models.Teacher).filter(models.Teacher.full_name == full_name).first()


def get_teacher_by_id(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Teacher).offset(skip).limit(limit).all()


def create_teacher(db: Session, teacher: schemas.TeacherBase):
    db_teacher = models.Teacher(full_name=teacher.full_name)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def delete_teacher(
        db: Session,
        teacher_id: int
):
    try:
        teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).one()
        db.delete(teacher)
        db.commit()
        return{"detail": "User successfully deleted"}
    except NoResultFound:
        db.rollback()
        return {"detail": "User not found"}


# def get_services(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Service).offset(skip).limit(limit).all()


# def create_teacher_service(db: Session, service: schemas.Service, teacher_id: int):
#     db_service = models.Service(**service.model_dump(), teacher_id=teacher_id)
#     db.add(db_service)
#     db.commit()
#     db.refresh(db_service)
#     return db_service