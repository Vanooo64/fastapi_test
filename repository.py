from database import new_session, TaskOrm
from schemas import TaskShema, TaskShemaAdd
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskShemaAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump() #робить у вигляді словника

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id



    @classmethod
    async def find_all(cls) -> list[TaskShema]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [TaskShema.model_validate(task_model) for task_model in task_models]
            return task_schemas
