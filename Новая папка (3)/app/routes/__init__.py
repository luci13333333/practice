from .admin import router as admin_router
from .student import student_router
from fastapi import APIRouter

# Создаем основной роутер
main_router = APIRouter()

# Добавляем все подроутеры
main_router.include_router(
    admin_router,
    prefix="/admin",
    tags=["admin"]
)

main_router.include_router(
    student_router,
    prefix="/student",
    tags=["student"]
)