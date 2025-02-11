from database import Base, engine
from app.models.user import Role
from app.models.student import Group

Base.metadata.create_all(bind=engine)

# Инициализация базовых данных
db = next(get_db())
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