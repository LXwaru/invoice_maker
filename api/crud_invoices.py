from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from datetime import datetime, timezone

from . import models, schemas


def create_invoice(
        db: Session,
        invoice: schemas.InvoiceCreate
):
    
    try:
        client_id = invoice.client_id
        start_date = invoice.start_date
        end_date = invoice.end_date

        print(f"received invoice data: client_id={client_id}, start_date={start_date}, end_date={end_date}")

        if start_date.tzinfo is None:
            start_date = start_date.replace(tzinfo=timezone.utc)
        if end_date.tzinfo is None:
            end_date = end_date.replace(tzinfo=timezone.utc)

        total_amount = (
            db.query(func.sum(models.Service.price))
            .join(models.ServiceItem, models.Service.id == models.ServiceItem.service_id)
            .filter(models.ServiceItem.client_id == client_id)
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
            client_id = client_id,
            start_date = start_date,
            end_date = end_date
        )
        db.add(new_invoice)
        db.commit()
        db.refresh(new_invoice)

        service_items = db.query(models.ServiceItem).filter(
            models.ServiceItem.client_id == client_id,
            models.ServiceItem.date_time >= start_date,
            models.ServiceItem.date_time <= end_date
        ).all()

        db.query(models.ServiceItem).filter(
            models.ServiceItem.client_id == client_id,
            models.ServiceItem.date_time >= start_date,
            models.ServiceItem.date_time <= end_date
        ).update({'invoice_id': new_invoice.id})

        db.commit()

        service_items_out = [
            schemas.ServiceItemOut(
                id=item.id,
                client_id=item.client_id,
                service_id=item.service_id,
                date_time=item.date_time
            ) for item in service_items
        ]

        return schemas.Invoice(
            id=new_invoice.id,
            client_id=new_invoice.client_id,
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


def add_service_item_to_invoice(
        db: Session,
        invoice_id: int,
        service_item: schemas.ServiceItemIn
):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).one()
    if not invoice:
        raise HTTPException(status_code=404, detail="invoice not found")
    
    new_service_item = models.ServiceItem(**service_item.model_dump(), invoice_id=invoice.id)
    db.add(new_service_item)
    db.commit()
    db.refresh(new_service_item)

    updated_service_prices = 0
    for service_item in invoice.service_items:
        service = db.query(models.Service).filter(models.Service.id == service_item.service_id).one()
        updated_service_prices += service.price
    invoice.amount_due = updated_service_prices
    db.commit()
    db.refresh(invoice)
    return invoice



def delete_invoice(
        db: Session,
        invoice_id: int
):
    try: 
        invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).one()
        db.delete(invoice)
        db.commit()
        return{"detail": "invoice deleted"}
    except NoResultFound:
        db.rollback()
        return {"detail": "invoice not found"}
