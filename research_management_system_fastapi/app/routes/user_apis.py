from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.config import SessionLocal
from ..schemas.user_schema import UserSchema, UpdateUserSchema
from ..crud.user_crud import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users", tags=["Users"])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip, limit)


@router.get("/users/{user_id}", tags=["Users"])
def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", tags=["Users"])
def add_user(user: UserSchema, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.put("/users/{user_id}", tags=["Users"])
def modify_user(user_id: int, user: UpdateUserSchema, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user.dict(exclude_unset=True))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/users/{user_id}", tags=["Users"])
def remove_user(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
