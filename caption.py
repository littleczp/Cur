import subprocess

from dataset import dataset_path_prefix


def captions(task_id: str):
    upload_cmd = f"cd kohya_ss && python finetune/make_captions.py --batch_size 8 {dataset_path_prefix}/{task_id}"
    p = subprocess.Popen(upload_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret = p.wait()
    print("captions result, code: ", ret)
    print("captions result: ", p.stdout.read())
    print("captions error: ", p.stderr.read())
