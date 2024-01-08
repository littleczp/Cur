from ali_oss import percentage, model_bucket

from db.task import update_task
from main import TaskStatus


def upload_sdxl(task_id: str):
    # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
    file_path = f"{task_id}.safetensors",
    model_bucket.put_object_from_file(
        file_path,
        f"/root/autodl-tmp/sdxl/model/{task_id}.safetensors",
        progress_callback=percentage
    )
    update_task(task_id, TaskStatus.finish, file_path)
