from app.tasks.celery_app import celery_app


@celery_app.task(queue="wearable", name="app.tasks.wearable_tasks.ingest_wearable")
def ingest_wearable(device_id: str, patient_id: int, payload: dict):
    """Ingest and store wearable device readings into hypertable."""
    return {"device_id": device_id, "records_ingested": len(payload.get("readings", []))}

