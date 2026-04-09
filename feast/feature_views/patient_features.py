from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64, String

patient_entity = Entity(name="patient_id", description="Unique patient identifier")

patient_source = FileSource(
    path="data/patient_features.parquet",
    timestamp_field="event_timestamp",
)

patient_feature_view = FeatureView(
    name="patient_demographics",
    entities=[patient_entity],
    ttl=timedelta(days=30),
    schema=[
        Field(name="age", dtype=Int64),
        Field(name="bmi", dtype=Float32),
        Field(name="gender", dtype=String),
        Field(name="blood_type", dtype=String),
    ],
    online=True,
    source=patient_source,
)
