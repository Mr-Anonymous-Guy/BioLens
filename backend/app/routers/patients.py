from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models.patient import Patient
from app.models.user import User
from app.schemas.patient import PatientMeResponse, PatientSummary

router = APIRouter()


@router.get("/me", response_model=PatientMeResponse)
def get_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.user_id == current_user.id).first()
    return PatientMeResponse(
        user_id=current_user.id,
        email=current_user.email,
        full_name=current_user.full_name,
        role=current_user.role,
        patient=PatientSummary.model_validate(patient) if patient else None,
    )

