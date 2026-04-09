from typing import Any

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    patient_id: int
    disease_type: str
    features: dict[str, Any] = Field(default_factory=dict)


class PredictionResponse(BaseModel):
    patient_id: int
    disease_type: str
    risk_score: float
    risk_label: str
    model_version: str = "baseline-v1"
    cached: bool = False
    features_used: dict[str, Any] = Field(default_factory=dict)

