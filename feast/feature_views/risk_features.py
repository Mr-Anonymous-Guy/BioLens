from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, String

patient_entity = Entity(name="patient_id")
risk_source = FileSource(path="data/risk_features.parquet", timestamp_field="event_timestamp")

risk_feature_view = FeatureView(
    name="risk_scores",
    entities=[patient_entity],
    ttl=timedelta(days=7),
    schema=[
        Field(name="diabetes_risk", dtype=Float32),
        Field(name="cvd_risk", dtype=Float32),
        Field(name="hypertension_risk", dtype=Float32),
        Field(name="nafld_risk", dtype=Float32),
        Field(name="ckd_risk", dtype=Float32),
        Field(name="composite_risk_label", dtype=String),
    ],
    online=True,
    source=risk_source,
)
