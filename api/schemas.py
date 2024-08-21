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
    teacher_id: int
    service_id: int

class ServiceItemOut(ServiceItemIn):
    id: int
    date_time: datetime

    class Config:
        orm_mode = True


class TeacherBase(BaseModel):
    full_name: str


class Teacher(TeacherBase):
    id: int
    service_items: list[ServiceItemOut] = []

    class Config:
        orm_mode = True


class InvoiceCreate(BaseModel):
    teacher_id: int
    start_date: datetime
    end_date: datetime


class Invoice(InvoiceCreate):
    id: int
    amount_due: int
    paid: bool
    service_items: list[ServiceItemOut] = []

    class Config:
        orm_mode = True