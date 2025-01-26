from typing import Optional

from pydantic import BaseModel


class TaskShemaAdd(BaseModel):
    name: str
    description: Optional[str] = None

class TaskShema(TaskShemaAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int