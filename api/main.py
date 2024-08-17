from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal

from . import (
    routers_teachers, 
    routers_services, 
    routers_service_item, 
    routers_invoices
)


app = FastAPI()
app.include_router(routers_teachers.router, tags=["TEACHERS"])
app.include_router(routers_services.router, tags=["SERVICES"])
app.include_router(routers_service_item.router, tags=["SERVICE_ITEMS"])
app.include_router(routers_invoices.router, tags=["INVOICES"])

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response