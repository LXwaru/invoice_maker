from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import func

from . import models


def create_invoice(
        db: Session,
        teacher_id: int,
        start_date: datetime,
        end_date: datetime
):
    total_amount = (
        db.query(func.sum(models.Service.price))
        .join(models.ServiceItem, models.Service.id == models.ServiceItem.service_id)
        .filter(models.ServiceItem.teacher_id == teacher_id)
        .filter(models.ServiceItem.date_time >= start_date)
        .filter(models.ServiceItem.date_time <= end_date)
        .scalar()
    )

    # Set total_amount to 0 if no service items match the criteria
    if total_amount is None:
        total_amount = 0

    new_invoice = models.Invoice(
        amount_due=total_amount,
        paid = False,
        teacher_id = teacher_id,
        start_date = start_date,
        end_date = end_date
    )
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice
