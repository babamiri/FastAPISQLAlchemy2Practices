import uuid
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class Course(BaseModel):
    """Course model."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str


class CourseSchema(BaseModel):
    """Course schema model."""

    name: str = Field(min_length=1, max_length=127)


class Student(BaseModel):
    """Student model."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    courses: list[Course]


class StudentSchema(BaseModel):
    """Student schema model."""

    name: str = Field(min_length=1, max_length=127)
    family: Optional[str] = Field(min_length=1, max_length=127)
    courses: list[uuid.UUID] = Field(min_length=1)