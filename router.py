from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import TaskShemaAdd, TaskShema, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)

@router.post("")
async def add_task(
        task: Annotated[TaskShemaAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[TaskShema]:
    task = await TaskRepository.find_all()
    return task