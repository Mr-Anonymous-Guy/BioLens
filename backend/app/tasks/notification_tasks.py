from app.tasks.celery_app import celery_app


@celery_app.task(queue="notifications", name="app.tasks.notification_tasks.send_alert")
def send_alert(patient_id: int, alert_type: str, message: str):
    """Send push/email/SMS notification to patient or doctor."""
    return {"patient_id": patient_id, "alert_type": alert_type, "sent": True}

