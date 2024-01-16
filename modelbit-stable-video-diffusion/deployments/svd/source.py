import modelbit, sys
import cloudpickle
import torch

from typing import *
from diffusers.utils import load_image, export_to_video


with open('pipe-fp16.pkl', 'rb') as file:
    pipe = cloudpickle.load(file)
    
# main function
def svd(img_url):
    image = load_image(img_url)
    image = image.resize((1024, 576))

    generator = torch.manual_seed(42)
    frames = pipe(image, decode_chunk_size=8, generator=generator).frames[0]

    # export_to_video(frames, "generated.mp4", fps=7)

    for i in frames:
        modelbit.log_image(i)

    return {'output': 'Success.'}

# to run locally via git & terminal, uncomment the following lines
# if __name__ == "__main__":
#   print(mistral_prompt(*(modelbit.parseArg(v) for v in sys.argv[1:])))
