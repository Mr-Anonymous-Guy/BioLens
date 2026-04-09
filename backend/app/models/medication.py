from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String

from app.database import Base
from app.models.base import TimestampMixin


class Medication(TimestampMixin, Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    drug_name = Column(String(255))
    dosage = Column(String(100))
    frequency = Column(String(100))
    route = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)
    prescribed_by = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)


class MedicationAdherence(Base):
    __tablename__ = "medication_adherence"

    id = Column(Integer, primary_key=True)
    medication_id = Column(Integer, ForeignKey("medications.id"), index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    scheduled_at = Column(DateTime(timezone=True))
    taken_at = Column(DateTime(timezone=True))
    taken = Column(Boolean, default=False)

