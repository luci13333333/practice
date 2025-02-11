from sqlalchemy.orm import sessionmaker
from config import Config
from database import engine


def get_db():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    from app.models.user import Role
    from app.models.student import Group

    db = next(get_db())

    # Создание ролей
    roles = ["admin", "student", "teacher"]
    for role_name in roles:
        role = db.query(Role).filter(Role.role_name == role_name).first()
        if not role:
            role = Role(role_name=role_name)
            db.add(role)
            db.commit()

    # Создание базовой группы
    group = db.query(Group).filter(Group.group_id == 1).first()
    if not group:
        group = Group(group_name="ПИ-101", course=1)
        db.add(group)
        db.commit()