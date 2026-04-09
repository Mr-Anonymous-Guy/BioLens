from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.core.qdrant_client import create_collection_if_not_exists
from app.routers import auth, health, patients, predictions

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(patients.router, prefix="/api/v1/patients", tags=["patients"])
app.include_router(
    predictions.router, prefix="/api/v1/predictions", tags=["predictions"]
)
app.include_router(health.router, prefix="/api", tags=["health"])


@app.on_event("startup")
def startup_event():
    create_collection_if_not_exists()

