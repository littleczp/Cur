from ali_oss import percentage, model_bucket


def upload_sdxl(task_id: str):
    # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
    model_bucket.put_object_from_file(
        f"{task_id}.safetensors",
        f"/root/autodl-tmp/sdxl/model/{task_id}.safetensors",
        progress_callback=percentage
    )
