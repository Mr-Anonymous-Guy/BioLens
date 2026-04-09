from app.tasks.celery_app import celery_app


@celery_app.task(queue="report", name="app.tasks.report_tasks.generate_report")
def generate_report(patient_id: int, report_type: str):
    """Generate PDF health report for patient."""
    return {"patient_id": patient_id, "report_type": report_type, "url": "/reports/..."}

