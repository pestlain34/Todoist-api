import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from enum import Enum

class Error(BaseModel):
    detail:Optional[str] = None

class Priority(str , Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class Status(str , Enum):
    pending = 'pending'
    progress = 'progress'
    completed = 'completed'
class CreateTaskSchema(BaseModel):
    priority: Optional[Priority] = Priority.low
    status: Optional[Status] = Status.pending
    task: str

class GetTaskSchema(BaseModel):
    id: uuid.UUID
    created: datetime
    updated: datetime
    priority: Priority
    status: Status
    task: str
    user_id: uuid.UUID

    class Config:
        from_attributes = True


class UserCreateSchema(BaseModel):
    email: str

class UserSchema(UserCreateSchema):
    id: uuid.UUID
    created: datetime

    class Config:
        from_attributes = True

