from pydantic import BaseModel
from datetime import datetime
from typing import Union, List


class ServiceIn(BaseModel):
    title: str
    price: int


class ServiceOut(ServiceIn):
    id: int

    class Config:
        orm_mode = True
    

class ServiceItemIn(BaseModel):
    employee_id: int
    client_id: int
    service_id: int

class ServiceItemOut(ServiceItemIn):
    id: int
    date_time: datetime

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    full_name: str
    email: str
    
class Client(ClientBase):
    id: int
    service_items: list[ServiceItemOut] = []

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    full_name: str
    email: str


class Employee(EmployeeBase):
    id: int
    is_active: bool
    service_items: list[ServiceItemOut] = []

    class Config:
        orm_mode = True


class InvoiceCreate(BaseModel):
    employee_id: int
    client_id: int
    start_date: datetime
    end_date: datetime


class Invoice(InvoiceCreate):
    id: int
    amount_due: int
    paid: bool
    service_items: list[ServiceItemOut] = []

    class Config:
        orm_mode = True
