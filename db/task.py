import enum

from db.db import DBInstance, Collection


# 模型训练任务
class TaskState(str, enum.Enum):
    RUNNING = "running"
    FAILED = "failed"
    FINISH = "finish"


# 更新模型训练任务状态
def update_task(task_id: str, state: TaskState, model_path: str):
    task = DBInstance.with_collection(Collection.TASK).find_one({
        'task_id': task_id
    })
    if task is None:
        DBInstance.with_collection(Collection.TASK).insert_one({
            'task_id': task_id,
            'state': state,
            'path': model_path

        })
    else:
        DBInstance.with_collection(Collection.TASK).update_one({
            'task_id': task_id
        }, {
            'state': state,
            'path': model_path
        })


# 获取模型训练任务状态
def get_task(task_id: str):
    return DBInstance.with_collection(Collection.TASK).find_one({
        'task_id': task_id
    })
