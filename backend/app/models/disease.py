from sqlalchemy import Boolean, Column, Date, ForeignKey, Float, Integer, String

from app.database import Base
from app.models.base import TimestampMixin


class DiabetesProfile(TimestampMixin, Base):
    __tablename__ = "diabetes_profiles"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), unique=True, index=True)
    hba1c = Column(Float)
    fasting_glucose = Column(Float)
    ppg_2hr = Column(Float)
    diabetes_type = Column(String(20))
    diagnosed_date = Column(Date)
    on_insulin = Column(Boolean, default=False)


class CardiovascularProfile(Base):
    __tablename__ = "cardiovascular_profiles"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), unique=True, index=True)
    ejection_fraction = Column(Float)
    lvef = Column(Float)
    echo_date = Column(Date)
    stress_test_result = Column(String(50))
    prior_mi = Column(Boolean, default=False)


class HypertensionProfile(Base):
    __tablename__ = "hypertension_profiles"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), unique=True, index=True)
    avg_systolic = Column(Float)
    avg_diastolic = Column(Float)
    stage = Column(String(20))
    antihypertensive_meds = Column(Boolean, default=False)


class NafldProfile(Base):
    __tablename__ = "nafld_profiles"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), unique=True, index=True)
    alt_level = Column(Float)
    ast_level = Column(Float)
    fibrosis_score = Column(Float)
    liver_fat_pct = Column(Float)
    fibroscan_date = Column(Date)


class CkdProfile(Base):
    __tablename__ = "ckd_profiles"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), unique=True, index=True)
    egfr = Column(Float)
    creatinine = Column(Float)
    uacr = Column(Float)
    ckd_stage = Column(Integer)
    dialysis = Column(Boolean, default=False)

