from fastapi import FastAPI, Request
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

@app.middleware('http')
async def some_middleware(request: Request, call_next):
    if (
        not os.path.exists("../Front/dist"+request.url.path) and
        not request.url.path.startswith("/openapi.json" ) and 
        not request.url.path.startswith("/api" ) and
        not request.url.path.startswith("/docs" ) and
        not request.url.path.startswith("/redoc" )
        ):
        request.scope['path'] = '/'
        headers = dict(request.scope['headers'])
        request.scope['headers'] = [(k, v) for k, v in headers.items()]
    
    return await call_next(request)


# Serve Vue app in production
app.mount("/", StaticFiles(directory="../Front/dist", html=True), name="static")
