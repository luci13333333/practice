from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.auth import get_current_active_user, hash_password
from app.models.user import User, Role
from app.models.student import Student
from app.models.subject import SemesterSubject
from typing import List

router = APIRouter()


@router.post("/register/")
def register_admin(
        email: str,
        password: str,
        db: Session = Depends(get_db)
):
    # Создание роли админа если её нет
    admin_role = db.query(Role).filter(Role.role_name == "admin").first()
    if not admin_role:
        admin_role = Role(role_name="admin")
        db.add(admin_role)
        db.commit()

    # Проверка существования пользователя
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже существует"
        )

    # Создание администратора
    hashed_password = hash_password(password)
    user = User(email=email, password_hash=hashed_password, role_id=admin_role.role_id)
    db.add(user)
    db.commit()
    return {"message": "Администратор успешно создан"}