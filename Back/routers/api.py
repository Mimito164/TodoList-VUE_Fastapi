from fastapi import APIRouter


router = APIRouter(
    prefix="/api"
)

@router.get("/")
async def root():
    return {"msg":"xd"}

@router.get("/v1/health")
async def health_check():
    return {"status": "healthy"}

