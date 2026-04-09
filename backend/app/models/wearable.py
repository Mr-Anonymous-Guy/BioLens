from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, JSON, String

from app.database import Base


class WearableReading(Base):
    __tablename__ = "wearable_readings"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    device_id = Column(String(100))
    device_type = Column(String(50))
    metric_name = Column(String(100))
    metric_value = Column(Float)
    unit = Column(String(20))
    recorded_at = Column(DateTime(timezone=True), index=True)
    raw_payload = Column(JSON)


class WearableDevice(Base):
    __tablename__ = "wearable_devices"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), index=True)
    device_id = Column(String(100), unique=True)
    device_name = Column(String(255))
    manufacturer = Column(String(100))
    model = Column(String(100))
    registered_at = Column(DateTime(timezone=True))
    is_active = Column(Boolean, default=True)

