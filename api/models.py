from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    services = relationship("Services", back_populates="teacher")
    invoices = relationship("Invoices", back_populates="teacher")


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    price = Column(Integer, index=True)
    date_completed = Column(datetime, index=True)

    def __repr__(self):
        return f"<Service(title='{self.title}', price='{self.price}')>"
    

class ServiceItem(Base):
    __tablename__ = "service_items"

    id = id = Column(Integer, primary_key=True)
    item = Column(String, index=True)
    date_completed = Column(datetime, index=True)
    teacher_id = Column(Integer, ForeignKey("teacher.id"))

    teacher = relationship("teacher", back_populates=("service"))


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    amount_due = Column(Integer, index=True)
    paid = Column(Boolean, index=True)
    teacher_id = Column(Integer, ForeignKey("teacher.id"))
    service_item_id = Column(Integer, ForeignKey('service_items.id'))

    teacher = relationship("Teacher", back_populates="invoice")
    services = relationship("Services", back_populates="invoice")

