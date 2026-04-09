from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, JSON, String, Text

from app.database import Base
from app.models.base import TimestampMixin


class Prediction(TimestampMixin, Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    disease_type = Column(String(50))
    risk_score = Column(Float)
    risk_label = Column(String(20))
    model_version = Column(String(50))
    features_used = Column(JSON)
    shap_values = Column(JSON)
    counterfactuals = Column(JSON)
    confidence = Column(Float)


class PredictionAlert(Base):
    __tablename__ = "prediction_alerts"

    id = Column(Integer, primary_key=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    alert_type = Column(String(50))
    message = Column(Text)
    acknowledged = Column(Boolean, default=False)
    sent_at = Column(DateTime(timezone=True))

