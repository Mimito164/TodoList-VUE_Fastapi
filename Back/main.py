from fastapi import FastAPI
from .routers import api
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .db.client import uri

app = FastAPI()

app.include_router(api.router)


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Serve Vue app in production
app.mount("/", StaticFiles(directory="../Front/dist", html=True), name="static")


