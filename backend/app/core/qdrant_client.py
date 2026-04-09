import logging

try:
    from qdrant_client import QdrantClient
    from qdrant_client.models import Distance, PointStruct, VectorParams
except ImportError:  # pragma: no cover - optional local dependency
    QdrantClient = None  # type: ignore[assignment]
    Distance = PointStruct = VectorParams = None  # type: ignore[assignment]

from app.config import settings

logger = logging.getLogger(__name__)

_client: QdrantClient | None = None

COLLECTION_NAME = settings.QDRANT_COLLECTION
VECTOR_DIM = 1024


def get_qdrant_client() -> QdrantClient:
    if QdrantClient is None:  # pragma: no cover - optional local dependency
        raise RuntimeError("qdrant-client is not installed")

    global _client
    if _client is None:
        _client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
    return _client


def create_collection_if_not_exists() -> bool:
    if QdrantClient is None:  # pragma: no cover - optional local dependency
        logger.warning("Skipping Qdrant bootstrap: qdrant-client is not installed")
        return False

    try:
        client = get_qdrant_client()
        existing = [collection.name for collection in client.get_collections().collections]
        if COLLECTION_NAME not in existing:
            client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=VECTOR_DIM, distance=Distance.COSINE),
            )
            logger.info("Collection '%s' created", COLLECTION_NAME)
        return True
    except Exception as exc:  # pragma: no cover - runtime safety
        logger.warning("Skipping Qdrant bootstrap: %s", exc)
        return False


def upsert_embedding(point_id: str, vector: list[float], payload: dict):
    client = get_qdrant_client()
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[PointStruct(id=point_id, vector=vector, payload=payload)],
    )


def search_similar(query_vector: list[float], top_k: int = 5):
    client = get_qdrant_client()
    return client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k,
    )
