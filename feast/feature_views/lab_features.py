from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32

patient_entity = Entity(name="patient_id")
lab_source = FileSource(path="data/lab_features.parquet", timestamp_field="event_timestamp")

lab_feature_view = FeatureView(
    name="lab_biomarkers",
    entities=[patient_entity],
    ttl=timedelta(days=90),
    schema=[
        Field(name="hba1c", dtype=Float32),
        Field(name="fasting_glucose", dtype=Float32),
        Field(name="total_cholesterol", dtype=Float32),
        Field(name="ldl", dtype=Float32),
        Field(name="hdl", dtype=Float32),
        Field(name="triglycerides", dtype=Float32),
        Field(name="creatinine", dtype=Float32),
        Field(name="egfr", dtype=Float32),
        Field(name="alt", dtype=Float32),
        Field(name="ast", dtype=Float32),
    ],
    online=True,
    source=lab_source,
)
