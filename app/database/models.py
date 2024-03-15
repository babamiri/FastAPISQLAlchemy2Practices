import uuid
from typing import Optional
from sqlalchemy import Column, ForeignKey, Table, orm
from sqlalchemy.dialects.postgresql import UUID


class Base(orm.DeclarativeBase):
    """Base database model."""

    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    


student_course_association = Table(
    "student_corse",
    Base.metadata,
    Column("student_id", UUID(as_uuid=True), ForeignKey("student.id")),
    Column("course_id", UUID(as_uuid=True), ForeignKey("course.id")),
)


class Course(Base):
    """Course database model."""

    __tablename__ = "course"

    name: orm.Mapped[str]


class Student(Base):
    """Student database model."""

    __tablename__ = "student"

    name: orm.Mapped[str]
    family: orm.Mapped[Optional[str]]
    courses: orm.Mapped[list["Course"]] = orm.relationship(
        secondary=student_course_association,
        backref="students",
        lazy="selectin",
    )