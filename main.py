
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("БД очищена")
    await create_tables()
    print("БД готова до роботи")
    yield
    print("Вимкнення")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)

print("ds")





