import os
from typing import List
from ali_oss import percentage, user_bucket

dataset_path_prefix = "/root/autodl-tmp/sdxl/dataset/training_images"


def get_dataset(task_id: str, train_path: List[str]):
    dataset_path = f"{dataset_path_prefix}/{task_id}"
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)

    for path in train_path:
        filename = f"{dataset_path}/{path}"
        user_bucket.get_object_to_file(
            path,
            filename,
            progress_callback=percentage
        )
        print("file_path: ", filename, end="\n")

    print("get dataset success")
