import json
import fnmatch
from dataclasses import dataclass, field

try:
    import redis
except ImportError:  # pragma: no cover - optional local dependency
    redis = None

from app.config import settings

if redis is not None:
    session_store = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
    cache_store = redis.Redis.from_url(
        settings.REDIS_URL.replace("/0", "/1"), decode_responses=True
    )
else:  # pragma: no cover - local fallback for development without Redis installed

    @dataclass
    class _MemoryRedis:
        store: dict[str, str] = field(default_factory=dict)

        def setex(self, key: str, ttl: int, value: str):
            self.store[key] = value

        def get(self, key: str):
            return self.store.get(key)

        def delete(self, *keys: str):
            for key in keys:
                self.store.pop(key, None)

        def keys(self, pattern: str):
            return [key for key in self.store if fnmatch.fnmatch(key, pattern)]

    session_store = _MemoryRedis()
    cache_store = _MemoryRedis()


def set_session(session_id: str, data: dict, ttl: int = 3600):
    session_store.setex(f"session:{session_id}", ttl, json.dumps(data))


def get_session(session_id: str) -> dict | None:
    raw = session_store.get(f"session:{session_id}")
    return json.loads(raw) if raw else None


def delete_session(session_id: str):
    session_store.delete(f"session:{session_id}")


def cache_prediction(patient_id: int, disease: str, result: dict, ttl: int = 900):
    key = f"prediction:{patient_id}:{disease}"
    cache_store.setex(key, ttl, json.dumps(result))


def get_cached_prediction(patient_id: int, disease: str) -> dict | None:
    key = f"prediction:{patient_id}:{disease}"
    raw = cache_store.get(key)
    return json.loads(raw) if raw else None


def invalidate_prediction_cache(patient_id: int):
    keys = cache_store.keys(f"prediction:{patient_id}:*")
    if keys:
        cache_store.delete(*keys)
