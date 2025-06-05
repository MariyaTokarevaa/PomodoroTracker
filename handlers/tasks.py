from typing import Annotated
from fastapi import APIRouter, status, Depends
from database import get_db_session
from schema.task import TaskSchema
from repository import TaskRepository, TaskCache
from dependency import get_tasks_repository, get_cache_tasks_repository, get_task_service
from database.models import Tasks
from service.task import TaskService


router = APIRouter(prefix="/task", tags=["task"])

@router.get("/tasks", response_model=list[TaskSchema])
async def get_tasks(task_service: Annotated[TaskService, Depends(get_task_service)]):
    return task_service.get_tasks()

@router.post("/add_task", response_model=TaskSchema)
async def create_task(task: TaskSchema,
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_model = Tasks(
        name=task.name,
        pomodoro_count=task.pomodoro_count,
        category_id=task.category_id
    )
    task_id = task_repository.create_task(task_model)
    task.id = task_id
    return task

@router.patch("/{task_id}", response_model=TaskSchema)
async def patch_task(
        task_id: int,
        name: str,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    return task_repository.update_task(task_id, name)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]):
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
        task_repository.delete_task(task_id)
        return {"message": "Task deleted successfully"}