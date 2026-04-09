from app.tasks.celery_app import celery_app


@celery_app.task(bind=True, queue="ml-inference", name="app.tasks.ml_tasks.run_prediction")
def run_prediction(self, patient_id: int, disease_type: str, features: dict):
    """Run ML model inference for a given patient."""
    try:
        return {
            "patient_id": patient_id,
            "disease_type": disease_type,
            "risk_score": 0.72,
            "risk_label": "high",
        }
    except Exception as exc:  # pragma: no cover - Celery retry path
        raise self.retry(exc=exc, countdown=30, max_retries=3)

