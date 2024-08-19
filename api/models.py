from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta

from .database import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    service_items = relationship("ServiceItem", back_populates="teacher")
    invoices = relationship("Invoice", back_populates="teacher")


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    price = Column(Integer, index=True)


class ServiceItem(Base):
    __tablename__ = "service_items"

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, default=datetime.now, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    service_id = Column(Integer, ForeignKey('services.id'))
    invoice_id = Column(Integer, ForeignKey('invoices.id'))

    teacher = relationship("Teacher", back_populates="service_items")
    service = relationship("Service")
    invoices = relationship("Invoice", back_populates="service_items")



class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    amount_due = Column(Integer, index=True)
    paid = Column(Boolean, default=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    start_date = Column(DateTime, index=True)
    end_date = Column(DateTime, index=True)

    teacher = relationship("Teacher", back_populates="invoices")
    service_items = relationship("ServiceItem", back_populates="invoices")

