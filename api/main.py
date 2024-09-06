from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal

from . import (
    routers_clients, 
    routers_services, 
    routers_service_item, 
    routers_invoices,
    routers_employees,
    routers_security,
    routers_companies,
    routers_users
)


app = FastAPI()
app.include_router(routers_clients.router, tags=["CLIENTS"])
app.include_router(routers_services.router, tags=["SERVICES"])
app.include_router(routers_service_item.router, tags=["SERVICE_ITEMS"])
app.include_router(routers_invoices.router, tags=["INVOICES"])
app.include_router(routers_employees.router, tags=["EMPLOYEES"])
app.include_router(routers_security.router, tags=["SECURITY"])
app.include_router(routers_companies.router, tags=["COMPANIES"])
app.include_router(routers_users.router, tags=["USERS"])


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