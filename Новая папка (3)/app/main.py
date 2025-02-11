from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import Config
from routes.admin import router
from routes.student import student_router
from database import Base
from routes import main_router

app = FastAPI(
    title="Система управления студентами",
    description="API для работы со студентами и оценками",
    version="1.0.0"
)

# Добавляем основной роутер
app.include_router(main_router)

# Создание движка и базы данных
engine = create_engine(Config.DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Регистрация роутов
app.include_router(router)
app.include_router(student_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)