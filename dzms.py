from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str

taskslist = {
        1: Task(id=1, name="task1"),
        2: Task(id=2, name="task2"),
        3: Task(id=3, name="task3"),
        4: Task(id=4, name="task4")
    }