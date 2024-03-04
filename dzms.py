from pydantic import BaseModel

class Task(BaseModel):
    name: str

taskslist = {
        1: Task(name="task1"),
        2: Task(name="task2"),
        3: Task(name="task3"),
        4: Task(name="task4")
    }