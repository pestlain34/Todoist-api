import datetime
import uuid

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid = True) , primary_key = True , default = uuid.uuid4)
    created = Column(DateTime , nullable = False , default = datetime.datetime.utcnow)
    email = Column(String , nullable = False , unique = True)
    tasks = relationship('Task' , back_populates = 'users')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(UUID(as_uuid=True) , primary_key = True , default = uuid.uuid4)
    created = Column(DateTime , nullable = False , default = datetime.datetime.utcnow())
    updated = Column(DateTime , nullable = False , default = datetime.datetime.utcnow())
    priority = Column(String , nullable = False)
    status =Column(String , nullable = False)
    task = Column(String , nullable = False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship("User" , back_populates="tasks")
