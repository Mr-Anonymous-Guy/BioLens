from celery import Celery
from kombu import Exchange, Queue

from app.config import settings

celery_app = Celery(
    "biolens",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=[
        "app.tasks.ocr_tasks",
        "app.tasks.ml_tasks",
        "app.tasks.baseline_tasks",
        "app.tasks.notification_tasks",
        "app.tasks.report_tasks",
        "app.tasks.wearable_tasks",
    ],
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True,
    task_routes={
        "app.tasks.ocr_tasks.*": {"queue": "ocr"},
        "app.tasks.ml_tasks.*": {"queue": "ml-inference"},
        "app.tasks.baseline_tasks.*": {"queue": "baseline"},
        "app.tasks.notification_tasks.*": {"queue": "notifications"},
        "app.tasks.report_tasks.*": {"queue": "report"},
        "app.tasks.wearable_tasks.*": {"queue": "wearable"},
    },
    task_queues=(
        Queue("ocr", Exchange("ocr"), routing_key="ocr"),
        Queue("ml-inference", Exchange("ml-inference"), routing_key="ml-inference"),
        Queue("baseline", Exchange("baseline"), routing_key="baseline"),
        Queue("notifications", Exchange("notifications"), routing_key="notifications"),
        Queue("report", Exchange("report"), routing_key="report"),
        Queue("wearable", Exchange("wearable"), routing_key="wearable"),
    ),
    worker_prefetch_multiplier=1,
    task_acks_late=True,
)

