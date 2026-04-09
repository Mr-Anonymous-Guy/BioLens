from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, JSON, String, Text

from app.database import Base
from app.models.base import TimestampMixin


class Patient(TimestampMixin, Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, index=True)
    mrn = Column(String(50), unique=True, index=True)
    date_of_birth = Column(Date)
    gender = Column(String(10))
    blood_type = Column(String(5))
    height_cm = Column(Float)
    weight_kg = Column(Float)
    phone = Column(String(20))
    address = Column(Text)
    emergency_contact = Column(JSON)
    insurance_id = Column(String(100))


class PatientConsent(Base):
    __tablename__ = "patient_consents"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    consent_type = Column(String(100))
    granted = Column(Boolean, default=False)
    granted_at = Column(DateTime(timezone=True))

