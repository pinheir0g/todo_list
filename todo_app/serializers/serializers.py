from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    id: Optional[int]
    title: str
    description: str
    done: bool = False


class Tasks(BaseModel):
    tasks: list[Task]
    count: int
