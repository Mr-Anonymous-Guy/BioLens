from typing import Any

from app.core.redis_client import cache_prediction, get_cached_prediction


def _score_from_features(features: dict[str, Any]) -> float:
    if not features:
        return 0.72

    numeric_values = [value for value in features.values() if isinstance(value, (int, float))]
    if not numeric_values:
        return 0.5

    average = sum(float(value) for value in numeric_values) / len(numeric_values)
    return max(0.0, min(1.0, average / 100.0))


def run_prediction(patient_id: int, disease_type: str, features: dict[str, Any]) -> dict[str, Any]:
    cached = get_cached_prediction(patient_id, disease_type)
    if cached:
        cached["cached"] = True
        return cached

    risk_score = round(_score_from_features(features), 2)
    if risk_score < 0.33:
        risk_label = "low"
    elif risk_score < 0.66:
        risk_label = "moderate"
    else:
        risk_label = "high"

    result = {
        "patient_id": patient_id,
        "disease_type": disease_type,
        "risk_score": risk_score,
        "risk_label": risk_label,
        "model_version": "baseline-v1",
        "cached": False,
        "features_used": features,
    }
    cache_prediction(patient_id, disease_type, result)
    return result

