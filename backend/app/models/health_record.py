from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, JSON, String, Text

from app.database import Base
from app.models.base import TimestampMixin


class HealthRecord(TimestampMixin, Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    record_type = Column(String(50))
    visit_date = Column(Date)
    chief_complaint = Column(Text)
    diagnosis = Column(Text)
    notes = Column(Text)
    icd10_codes = Column(JSON)
    doctor_id = Column(Integer, ForeignKey("users.id"))


class Vitals(Base):
    __tablename__ = "vitals"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    record_id = Column(Integer, ForeignKey("health_records.id"), index=True)
    systolic_bp = Column(Float)
    diastolic_bp = Column(Float)
    heart_rate = Column(Integer)
    temperature_c = Column(Float)
    spo2_pct = Column(Float)
    respiratory_rate = Column(Integer)
    measured_at = Column(DateTime(timezone=True), index=True)

