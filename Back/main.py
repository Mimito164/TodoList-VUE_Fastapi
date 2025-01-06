from fastapi import FastAPI, Request
from .routers import api
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .db.client import uri
import os

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

@app.middleware('http')
async def some_middleware(request: Request, call_next):
    if not os.path.exists(request.url.path) and  "/openapi.json" not in request.url.path and  "/api" not in request.url.path and  "/docs" not in request.url.path and  "/redoc" not in request.url.path:
        request.scope['path'] = '/'
        headers = dict(request.scope['headers'])
        # headers[b'custom-header'] = b'my custom header'
        request.scope['headers'] = [(k, v) for k, v in headers.items()]
        
    return await call_next(request)

# Serve Vue app in production
app.mount("/", StaticFiles(directory="../Front/dist", html=True), name="static")


