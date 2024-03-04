# Необходимо создать АР! для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи
# должна быть возможность указать статус (выполнена/не выполнена).

# АР! должен содержать следующие конечные точки:

# — GET /task — возвращает список всех задач.

# — GET /task/{id} — возвращает задачу с указанным идентификатором.

# — POST /task — добавляет новую задачу.

# — POST /task/{id} — обновляет задачу с указанным идентификатором.

# — DELETE /task/{id} — удаляет задачу с указанным идентификатором.

# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Рудапёс.

import logging, collections
from fastapi import FastAPI
# from pydantic import BaseModel
from dzms import *

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get('/')
def base():
    logger.info('API успешно загружено.')
    return ('Привет! Здесь ничего не происходит!')

@app.get('/tasks')
async def tasklist():
    logger.info('Список задач загружен.')
    return (taskslist)

@app.get('/tasks/{id}')
async def tasklist(id: int):
    if id in taskslist:
        logger.info('Данная задача загружена.')
        return (taskslist[id])
    else:
        logger.info('Данной задачи не существует.')
        return (taskslist)
    
@app.post('/tasks')
async def tasklist(name: Task):
    if id not in taskslist:
        taskslist[max(taskslist)+1] = name
        logger.info('Данная задача успешно добавлена.')
        return (taskslist)
    else:
        logger.info('Данная задача уже существует.')
        return (taskslist)

@app.put('/tasks/{id}')
async def tasklist(id: int, name: Task):
    if id in taskslist:
        taskslist[id] = name
        logger.info('Данная задача успешно изменена.')
        return (taskslist)
    else:
        logger.info('Данной задачи не существует.')
        return (taskslist)

@app.delete('/tasks/{id}')
async def tasklist(id: int):
    if id in taskslist:
        taskslist.pop(id)
        logger.info('Данная задача успешно удалена.')
        return (taskslist)
    else:
        logger.info('Данной задачи не существует.')
        return (taskslist)

# logger.info('Произошла ошибка. Повторите попытку.')