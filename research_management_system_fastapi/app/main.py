from fastapi import FastAPI
from .models.user import User
from .routes.user_apis import router
from .config.config import engine

User.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api/v1", tags=["user"])


