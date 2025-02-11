from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.auth import get_current_active_user
from app.models.student import Student, SemesterGrade, SemesterSubject
from typing import List

# Создаем роутер для студентов
student_router = APIRouter(
    prefix="/student",
    tags=["student"],
    dependencies=[Depends(get_current_active_user)]
)

@student_router.get("/profile/")
def read_profile(
    db: Session = Depends(get_db),
    current_user: Student = Depends(get_current_active_user)
):
    return current_user

@student_router.get("/grades/")
def read_grades(
    db: Session = Depends(get_db),
    current_user: Student = Depends(get_current_active_user)
):
    grades = db.query(SemesterGrade).filter(
        SemesterGrade.student_id == current_user.student_id
    ).all()
    return grades

@student_router.get("/schedule/")
def read_schedule(
    db: Session = Depends(get_db),
    current_user: Student = Depends(get_current_active_user)
):
    schedule = db.query(SemesterSubject).filter(
        SemesterSubject.semester == current_user.group.course
    ).all()
    return schedule