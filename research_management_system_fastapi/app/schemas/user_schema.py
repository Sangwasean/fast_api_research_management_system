from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    email: str
    is_active: bool = True

    class Config:
        orm_mode = True


class UpdateUserSchema(BaseModel):
    name: str | None = None
    email: str | None = None
    is_active: bool | None = None

    class Config:
        orm_mode = True
