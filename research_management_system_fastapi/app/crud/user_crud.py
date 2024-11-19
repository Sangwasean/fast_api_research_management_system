from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user_schema import UserSchema


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserSchema):
    new_user = User(
        name=user.name,
        email=user.email,
        is_active=user.is_active,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user_id: int, updated_data: dict):
    user_to_update = get_user_by_id(db, user_id)
    if not user_to_update:
        return None

    for key, value in updated_data.items():
        setattr(user_to_update, key, value)

    db.commit()
    db.refresh(user_to_update)
    return user_to_update


def delete_user(db: Session, user_id: int):
    user_to_delete = get_user_by_id(db, user_id)
    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()
        return True
    return False
