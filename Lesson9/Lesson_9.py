import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://Ivan:20250311@localhost:5432/Lesson9"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Тест на добавление студента
def test_add_student(db):
    new_student = Student(name="Alice", age=20)
    db.add(new_student)
    db.commit()
    assert new_student.id is not None  

    
    db.delete(new_student)
    db.commit()

# Тест на изменение возраста студента
def test_update_student_age(db):
    student = Student(name="Bob", age=22)
    db.add(student)
    db.commit()

    student.age = 23
    db.commit()
    assert student.age == 23

    db.delete(student)
    db.commit()

# Тест на удаление студента
def test_delete_student(db):
    student = Student(name="Charlie", age=21)
    db.add(student)
    db.commit()
    student_id = student.id  

    db.delete(student)
    db.commit()

    
    deleted_student = db.query(Student).filter(Student.id == student_id).first()
    assert deleted_student is None  
