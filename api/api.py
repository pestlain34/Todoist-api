import datetime
import uuid
from typing import List

from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from data_access.database import get_db
from api.schemas import GetTaskSchema, CreateTaskSchema, UserCreateSchema, UserSchema
from data_access.models import Task, User

router = APIRouter()
@router.get('/tasks' , response_model=List[GetTaskSchema])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.post('/tasks' , response_model = GetTaskSchema , status_code = status.HTTP_201_CREATED)
def create_task(task_data: CreateTaskSchema, db: Session = Depends(get_db)):
    test_user = db.query(User).first()
    if not test_user:
        test_user = User(email="default@example.com")
        db.add(test_user)
        db.commit()
        db.refresh(test_user)
    new_task = Task(
        priority=task_data.priority.value,
        status=task_data.status.value,
        task=task_data.task,
        user_id=test_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get('/todo/{task_id}' , response_model= GetTaskSchema)
def get_task(task_id: uuid.UUID , db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put('/todo/{task_id}' , response_model= GetTaskSchema)
def update_task(task_id: uuid.UUID , task_data: CreateTaskSchema ,  db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )

    db_task.updated = datetime.datetime.utcnow()
    db_task.priority = task_data.priority.value
    db_task.status = task_data.status.value
    db_task.task = task_data.task

    db.commit()
    db.refresh(db_task)
    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )

    db.delete(db_task)
    db.commit()

@router.post('/users', response_model=UserSchema)
def create_user(user_data: UserCreateSchema, db: Session = Depends(get_db)):
    new_user = User(email=user_data.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/users', response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()