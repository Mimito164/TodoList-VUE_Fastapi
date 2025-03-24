from fastapi import FastAPI
from routers import api
from fastapi.middleware.cors import CORSMiddleware


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
