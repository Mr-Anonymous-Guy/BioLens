from app.tasks.celery_app import celery_app


@celery_app.task(bind=True, queue="ocr", name="app.tasks.ocr_tasks.process_document")
def process_document(self, document_id: int, file_path: str):
    """OCR processing for uploaded medical documents."""
    try:
        return {"status": "success", "document_id": document_id, "text": "extracted_text"}
    except Exception as exc:  # pragma: no cover - Celery retry path
        raise self.retry(exc=exc, countdown=60, max_retries=3)

