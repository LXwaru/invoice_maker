from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from datetime import datetime, timezone

from . import models, schemas


def create_invoice(
        db: Session,
        invoice: schemas.InvoiceCreate
):
    
    try:

        teacher_id = invoice.teacher_id
        start_date = invoice.start_date
        end_date = invoice.end_date

        print(f"received invoice data: teacher_id={teacher_id}, start_date={start_date}, end_date={end_date}")

        if start_date.tzinfo is None:
            start_date = start_date.replace(tzinfo=timezone.utc)
        if end_date.tzinfo is None:
            end_date = end_date.replace(tzinfo=timezone.utc)

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

        service_items = db.query(models.ServiceItem).filter(
            models.ServiceItem.teacher_id == teacher_id,
            models.ServiceItem.date_time >= start_date,
            models.ServiceItem.date_time <= end_date
        ).all()

        db.query(models.ServiceItem).filter(
            models.ServiceItem.teacher_id == teacher_id,
            models.ServiceItem.date_time >= start_date,
            models.ServiceItem.date_time <= end_date
        ).update({'invoice_id': new_invoice.id})

        db.commit()

        service_items_out = [
            schemas.ServiceItemOut(
                id=item.id,
                teacher_id=item.teacher_id,
                service_id=item.service_id,
                date_time=item.date_time
            ) for item in service_items
        ]

        return schemas.Invoice(
            id=new_invoice.id,
            teacher_id=new_invoice.teacher_id,
            start_date=new_invoice.start_date,
            end_date=new_invoice.end_date,
            amount_due=new_invoice.amount_due,
            paid=new_invoice.paid,
            service_items=service_items_out
    )

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=422, detail=f"An error occurred while creating the invoice: {str(e)}")


def list_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Invoice).offset(skip).limit(limit).all()


def get_one_invoice(db: Session, invoice_id: int):
    return db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()