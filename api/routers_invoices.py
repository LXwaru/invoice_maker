from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from datetime import datetime, timedelta
from . import schemas, crud_invoices, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/invoices/', response_model=schemas.Invoice)
def create_invoice(
    invoice: schemas.InvoiceCreate,
    db: Session = Depends(utils_db.get_db)
):
    return crud_invoices.create_invoice(
        db=db, invoice=invoice)


@router.get('/api/invoices/', response_model=list[schemas.Invoice])
def list_invoices(
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(utils_db.get_db)
):
    return crud_invoices.list_invoices(db=db, skip=skip, limit=limit)

@router.get('/api/invoice/{invoice_id}/', response_model=schemas.Invoice)
def get_one_invoice(
    invoice_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud_invoices.get_one_invoice(db=db, invoice_id=invoice_id)