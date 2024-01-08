from enum import Enum
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from dataset import get_dataset
from db.db import DBInstance
from db.task import update_task, get_task
from train import train_sdxl
from upload import upload_sdxl
from caption import captions

app = FastAPI()


class AIModel(BaseModel):
    log_id: str
    uid: str
    task_id: str
    train_path: List[str]
    callback_url: str
    user_sex: str


@app.post("/model/create")
def create_model(model: AIModel):
    # 读取训练集
    get_dataset(model.task_id, model.train_path)
    update_task(model.task_id, TaskStatus.trainging, "")

    # 训练集打标
    # captions(model.task_id)

    # 训练模型
    train_sdxl(model.task_id, model.user_sex)

    # 上传模型
    upload_sdxl(model.task_id)

    print("create model success")
    return {
        "code": 200,
        "msg": "success",
        "data": {
            "task_id": model.task_id,
            "model_uid": model.uid,
            "model_path": [""]
        }
    }


class TaskStatus(str, Enum):
    trainging = "under training"
    finish = "finish"
    error = "error"


@app.get("/model/mget")
def get_models(task_id: str):
    task = get_task(task_id)
    return {
        "code": 200,
        "msg": "success",
        "data": {
            'task_status': task['state'],
            'model_list': task['path']
        }
    }
