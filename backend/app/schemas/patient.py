from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class PatientSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int | None = None
    mrn: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None
    blood_type: str | None = None
    height_cm: float | None = None
    weight_kg: float | None = None
    phone: str | None = None
    address: str | None = None
    insurance_id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class PatientMeResponse(BaseModel):
    user_id: int
    email: str
    full_name: str | None = None
    role: str | None = None
    patient: PatientSummary | None = None

