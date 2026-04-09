from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64

patient_entity = Entity(name="patient_id")
wearable_source = FileSource(
    path="data/wearable_features.parquet", timestamp_field="event_timestamp"
)

wearable_feature_view = FeatureView(
    name="wearable_vitals",
    entities=[patient_entity],
    ttl=timedelta(hours=24),
    schema=[
        Field(name="avg_heart_rate", dtype=Float32),
        Field(name="avg_spo2", dtype=Float32),
        Field(name="daily_steps", dtype=Int64),
        Field(name="sleep_hours", dtype=Float32),
        Field(name="hrv_ms", dtype=Float32),
    ],
    online=True,
    source=wearable_source,
)
