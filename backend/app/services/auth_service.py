from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.models.user import RefreshToken, User


def register_user(db: Session, email: str, password: str, full_name: str) -> tuple[str, str, User]:
    user = User(email=email, hashed_password=hash_password(password), full_name=full_name)
    db.add(user)
    db.commit()
    db.refresh(user)

    access_token = create_access_token({"sub": str(user.id), "email": user.email})
    refresh_token = create_refresh_token({"sub": str(user.id), "email": user.email})
    db.add(
        RefreshToken(
            user_id=user.id,
            token=refresh_token,
            expires_at=token_expiry_from_jwt(refresh_token),
        )
    )
    db.commit()
    return access_token, refresh_token, user


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def issue_token_pair(db: Session, user: User) -> tuple[str, str]:
    access_token = create_access_token({"sub": str(user.id), "email": user.email})
    refresh_token = create_refresh_token({"sub": str(user.id), "email": user.email})
    db.add(
        RefreshToken(
            user_id=user.id,
            token=refresh_token,
            expires_at=token_expiry_from_jwt(refresh_token),
        )
    )
    db.commit()
    return access_token, refresh_token


def revoke_refresh_token(db: Session, refresh_token: str) -> bool:
    token = db.query(RefreshToken).filter(RefreshToken.token == refresh_token).first()
    if token:
        token.revoked = True
        db.commit()
        return True
    return False


def token_expiry_from_jwt(token: str):
    from app.core.security import decode_token

    payload = decode_token(token)
    exp = payload.get("exp")
    if isinstance(exp, datetime):
        return exp.astimezone(timezone.utc)
    if isinstance(exp, (int, float)):
        return datetime.fromtimestamp(exp, tz=timezone.utc)
    return None

