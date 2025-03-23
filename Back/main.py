from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from .routers import api
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()

app.include_router(api.router)


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000","*"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
