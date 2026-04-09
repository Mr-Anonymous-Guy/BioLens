from fastapi import APIRouter, Depends

from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction_service import run_prediction

router = APIRouter()


@router.post("/run", response_model=PredictionResponse)
def predict(
    payload: PredictionRequest,
    current_user: User = Depends(get_current_user),
):
    result = run_prediction(payload.patient_id, payload.disease_type, payload.features)
    return PredictionResponse(**result)


@router.get("/status")
def status(current_user: User = Depends(get_current_user)):
    return {"status": "ready", "user_id": current_user.id}

