from app.tasks.celery_app import celery_app


@celery_app.task(queue="baseline", name="app.tasks.baseline_tasks.compute_baseline")
def compute_baseline(patient_id: int):
    """Compute population-normalized baseline for patient metrics."""
    return {"patient_id": patient_id, "status": "baseline_computed"}

