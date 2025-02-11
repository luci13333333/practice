from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False)
    course = Column(Integer, nullable=False)
    students = relationship("Student", back_populates="group")