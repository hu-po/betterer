import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

# Use the K-LMS scheduler here instead
# scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, scheduler=scheduler, use_auth_token=True)

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_auth_token=True)
pipe = pipe.to(device)

prompt = "a pixar style image of a white bengal cat in a teepee"
with autocast("cuda"):
    image = pipe(prompt)["sample"][0]  
    
image.save("/tmp/buboo.png")

# import torch

# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_auth_token=True)
# pipe = pipe.to(device)

# from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler

# model_id = "CompVis/stable-diffusion-v1-4"
# # Use the K-LMS scheduler here instead
# scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
# pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, use_auth_token=True)
# pipe = pipe.to("cuda")

