from xmlrpc.client import DateTime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    last_name = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100))
    group_id = Column(Integer, ForeignKey('groups.group_id'))
    user = relationship("User", back_populates="student")
    semester_grades = relationship("SemesterGrade", back_populates="student")


class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False)
    course = Column(Integer, nullable=False)


class SemesterSubject(Base):
    __tablename__ = 'semester_subjects'
    semester_subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String(200), nullable=False)
    semester = Column(Integer, nullable=False)
    academic_year = Column(Integer, nullable=False)
    grades = relationship("SemesterGrade", back_populates="subject")

    __table_args__ = (
        UniqueConstraint('subject_name', 'semester', 'academic_year'),
    )


class SemesterGrade(Base):
    __tablename__ = 'semester_grades'
    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    semester_subject_id = Column(Integer, ForeignKey('semester_subjects.semester_subject_id'))
    score = Column(DECIMAL(3, 1))
    date_recorded = Column(DateTime, default=datetime.utcnow)
    student = relationship("Student", back_populates="semester_grades")
    subject = relationship("SemesterSubject", back_populates="grades")