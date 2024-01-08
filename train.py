import subprocess

from dataset import dataset_path_prefix


def train_sdxl(task_id: str, user_sex: str):
    train_cmd = f"""
        accelerate launch --num_cpu_threads_per_process=10 "./sdxl_train.py" \
          --pretrained_model_name_or_path="/root/autodl-tmp/sdxl/juggernaut-xl.safetensors" \
          --train_data_dir="{dataset_path_prefix}/{task_id}" \
          --reg_data_dir="./kohya_ss/dataset/reg_images/{user_sex}" \
          --output_dir="/root/autodl-tmp/sdxl/model" \
          --output_name="{task_id}" \
          --flip_aug \
          --save_model_as="safetensors" \
          --train_batch_size=1 \
          --max_train_steps=2000 \
          --save_every_n_steps=500 \
          --optimizer_type="Adafactor" \
          --optimizer_args scale_parameter=False relative_step=False warmup_init=False \
          --xformers \
          --cache_latents \
          --cache_text_encoder_outputs \
          --lr_scheduler="constant_with_warmup" \
          --lr_warmup_steps="100" \
          --learning_rate="6e-6" \
          --resolution="1024,1024" \
          --enable_bucket \
          --min_bucket_reso="640" \
          --max_bucket_reso="2048" \
          --save_precision="fp16" \
          --mixed_precision="bf16" \
          --min_snr_gamma=5 \
          --gradient_checkpointing
    """
    upload_cmd = f"cd kohya_ss && {train_cmd}"
    p = subprocess.Popen(upload_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            print('Subprogram output: [{}]'.format(line))
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')
    ret = p.wait()
    print("train result, code: ", ret)
    print("train result: ", p.stdout.read())
    print("train error: ", p.stderr.read())
