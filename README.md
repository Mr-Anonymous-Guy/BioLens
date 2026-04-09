# BioLens

Phase 1 foundation scaffold for the BioLens predictive health intelligence platform.

## What is included

- FastAPI backend scaffold with JWT auth, health, patient, and prediction routes
- SQLAlchemy models and an initial Alembic migration
- Redis, RabbitMQ, Celery, Qdrant, TimescaleDB, and Nginx compose wiring
- Feast feature store skeleton
- GitHub Actions CI workflow

## Notes

- The backend is designed to be import-safe even if Qdrant is not reachable at startup.
- The TimescaleDB hypertable conversion for `wearable_readings` is still a manual post-migration step.
