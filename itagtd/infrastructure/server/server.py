from fastapi import FastAPI
from itagtd.interfaces import trends_router

app = FastAPI()

app.include_router(trends_router, prefix="/trends", tags=["trends"])
