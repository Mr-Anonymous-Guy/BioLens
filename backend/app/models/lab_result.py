from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String

from app.database import Base
from app.models.base import TimestampMixin


class LabResult(TimestampMixin, Base):
    __tablename__ = "lab_results"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    test_name = Column(String(255))
    test_code = Column(String(50))
    value = Column(Float)
    unit = Column(String(50))
    reference_low = Column(Float)
    reference_high = Column(Float)
    is_abnormal = Column(Boolean, default=False)
    collected_date = Column(Date)
    lab_name = Column(String(255))
    ordered_by = Column(Integer, ForeignKey("users.id"))


class Biomarker(Base):
    __tablename__ = "biomarkers"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    biomarker_name = Column(String(100))
    value = Column(Float)
    unit = Column(String(50))
    measured_at = Column(DateTime(timezone=True), index=True)
    source = Column(String(50))

