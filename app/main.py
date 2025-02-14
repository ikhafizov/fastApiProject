from fastapi import FastAPI
from app.routers import item_router

app = FastAPI()

app.include_router(item_router.router)

