from fastapi import APIRouter

router = APIRouter()

tasks = [
    {"id": 1, "title": "Aprender Docker", "done": False},
    {"id": 2, "title": "Configurar CI/CD", "done": True},
]

@router.get("/")
def get_tasks():
    return tasks

@router.post("/")
def create_task(title: str):
    new_task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(new_task)
    return new_task
