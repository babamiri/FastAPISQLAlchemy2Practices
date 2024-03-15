import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select,update
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.database import models as db_models
from app.database.session import get_db_session

router = APIRouter(prefix="/v1", tags=["Version 1"])


@router.post("/courses", status_code=status.HTTP_201_CREATED)
async def create_course(
    data: models.CourseSchema,
    session: AsyncSession = Depends(get_db_session),
) -> models.Course:
    course = db_models.Course(**data.model_dump())
    session.add(course)
    await session.commit()
    await session.refresh(course)
    return models.Course.model_validate(course)


@router.get("/courses", status_code=status.HTTP_200_OK)
async def get_courses(
    session: AsyncSession = Depends(get_db_session),
) -> list[models.Course]:
    courses = await session.scalars(select(db_models.Course))
    return [models.Course.model_validate(course) for course in courses]


@router.get("/courses/{id}", status_code=status.HTTP_200_OK)
async def get_course(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
) -> models.Course:
    course = await session.get(db_models.Course, id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course does not exist",
        )
    return models.Course.model_validate(course)

@router.put("/courses/{id}", status_code=status.HTTP_200_OK)
async def get_course(
    id: uuid.UUID,
    data: models.CourseSchema,
    session: AsyncSession = Depends(get_db_session),
) -> models.Course:
    course = await session.get(db_models.Course, id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course does not exist",
        )
    
    query = (
        update(db_models.Course)
        .where(db_models.Course.id == id)
        .values(
            name=data.name 
        )
        .returning(db_models.Course)
    )        
    await session.execute(query)

    return models.Course.model_validate(course)




@router.post("/students", status_code=status.HTTP_201_CREATED)
async def create_student(
    data: models.StudentSchema,
    session: AsyncSession = Depends(get_db_session),
) -> models.Student:
    data_dict = data.model_dump()
    courses = await session.scalars(
        select(db_models.Course).where(
            db_models.Course.id.in_(data_dict.pop("courses"))
        )
    )
    student = db_models.Student(**data_dict, courses=list(courses))
    session.add(student)
    await session.commit()
    await session.refresh(student)
    return models.Student.model_validate(student)


@router.get("/students", status_code=status.HTTP_200_OK)
async def get_students(
    session: AsyncSession = Depends(get_db_session),
) -> list[models.Student]:
    students = await session.scalars(select(db_models.Student))
    return [models.Student.model_validate(student) for student in students]


@router.delete("/students/{id}", status_code=status.HTTP_200_OK)
async def get_student(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
) -> models.Student:
    student = await session.get(db_models.Student, id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student does not exist",
        )
    await session.delete(student)

    

@router.get("/students/{id}", status_code=status.HTTP_200_OK)
async def get_student(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
) -> models.Student:
    student = await session.get(db_models.Student, id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student does not exist",
        )
    return models.Student.model_validate(student)