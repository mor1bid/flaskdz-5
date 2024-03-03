from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str

taskslist = [
        0,
        Task(id=1, name="task1"),
        Task(id=2, name="task2"),
        Task(id=3, name="task3"),
        Task(id=4, name="task4")
    ]