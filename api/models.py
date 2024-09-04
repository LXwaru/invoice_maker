from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TIMESTAMP, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from .database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    service_items = relationship("ServiceItem", back_populates="client")
    invoices = relationship("Invoice", back_populates="client")



class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    service_items = relationship("ServiceItem", back_populates="employee")
    invoices = relationship("Invoice", back_populates="employee")


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    price = Column(Numeric, index=True)


class ServiceItem(Base):
    __tablename__ = "service_items"

    id = Column(Integer, primary_key=True)
    date_time = Column(TIMESTAMP(timezone=True), default=datetime.now)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    service_id = Column(Integer, ForeignKey('services.id'))
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship("Client", back_populates="service_items")
    employee = relationship("Employee", back_populates="service_items")
    service = relationship("Service")
    invoice = relationship("Invoice", back_populates="service_items")



class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    amount_due = Column(Integer, index=True)
    paid = Column(Boolean, default=False)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    start_date = Column(DateTime, index=True)
    end_date = Column(DateTime, index=True)

    client = relationship("Client", back_populates="invoices")
    employee = relationship("Employee", back_populates="invoices")
    service_items = relationship("ServiceItem", back_populates="invoice")

