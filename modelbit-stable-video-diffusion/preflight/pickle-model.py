import torch
import cloudpickle

from diffusers import StableVideoDiffusionPipeline

pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16"
)
pipe.enable_model_cpu_offload()

with open('pipe-fp16.pkl', 'wb') as file:
    cloudpickle.dump(pipe, file)
