""" Generate audio from text

You can play the audio generated in linux with:

> aplay sample.wav

"""

import os
import torch
import torchaudio
import matplotlib.pyplot as plt
import numpy as np
from audio_diffusion_pytorch import DiffusionModel, UNetV0, VDiffusion, VSampler
from dmae.model import DMAE1d

SAMPLING_FREQUENCY = 48000
PROMPT = ['Egyptian Darbuka, Drums, Rythm, (Deluxe Edition), 2 of 4']

model = DMAE1d.from_pretrained("archinetai/dmae1d-ATC32-v3")
# Encode/decode audio
audio = torch.randn(1, 2, 2**18) # [batch, in_channels, length]
# latent = model.encode(audio) # Encode
# sample = model.decode(latent, num_steps=10) # Decode by sampling diffusion model conditioning on latent

noise = torch.randn(1, 2, 2**18)
sample = model.sample(
    noise,
    text=PROMPT,
    embedding_scale=5.0, # Higher for more text importance, suggested range: 1-15 (Classifier-Free Guidance Scale)
    num_steps=32 # Higher for better quality, suggested num_steps: 10-100
)


# model = DiffusionModel(
#     net_t=UNetV0, # The model type used for diffusion (U-Net V0 in this case)
#     in_channels=2, # U-Net: number of input/output (audio) channels
#     channels=[8, 32, 64, 128, 256, 512, 512, 1024, 1024], # U-Net: channels at each layer
#     factors=[1, 4, 4, 4, 2, 2, 2, 2, 2], # U-Net: downsampling and upsampling factors at each layer
#     items=[1, 2, 2, 2, 2, 2, 2, 4, 4], # U-Net: number of repeating items at each layer
#     attentions=[0, 0, 0, 0, 0, 1, 1, 1, 1], # U-Net: attention enabled/disabled at each layer
#     attention_heads=8, # U-Net: number of attention heads per attention item
#     attention_features=64, # U-Net: number of attention features per attention item
#     diffusion_t=VDiffusion, # The diffusion method used
#     sampler_t=VSampler, # The diffusion sampler used
#     # ... same as unconditional model
#     use_text_conditioning=True, # U-Net: enables text conditioning (default T5-base)
#     use_embedding_cfg=True, # U-Net: enables classifier free guidance
#     embedding_max_length=64, # U-Net: text embedding maximum length (default for T5-base)
#     embedding_features=768, # U-Net: text mbedding features (default for T5-base)
#     cross_attentions=[0, 0, 0, 1, 1, 1, 1, 1, 1], # U-Net: cross-attention enabled/disabled at each layer
# )

# # Train model with audio waveforms
# audio_wave = torch.randn(1, 2, 2**18) # [batch, in_channels, length]
# loss = model(
#     audio_wave,
#     text=sample_paper_prompt, # Text conditioning, one element per batch
#     embedding_mask_proba=0.1 # Probability of masking text with learned embedding (Classifier-Free Guidance Mask)
# )
# loss.backward()

# # Turn noise into new audio sample with diffusion
# noise = torch.randn(1, 2, 2**18)
# sample = model.sample(
#     noise,
#     text=PROMPT,
#     embedding_scale=5.0, # Higher for more text importance, suggested range: 1-15 (Classifier-Free Guidance Scale)
#     num_steps=32 # Higher for better quality, suggested num_steps: 10-100
# )

def plot_waveform(waveform, sample_rate):
    waveform = waveform.numpy()

    num_channels, num_frames = waveform.shape
    time_axis = torch.arange(0, num_frames) / sample_rate

    figure, axes = plt.subplots(num_channels, 1)
    if num_channels == 1:
        axes = [axes]
    for c in range(num_channels):
        axes[c].plot(time_axis, waveform[c], linewidth=1)
        axes[c].grid(True)
        if num_channels > 1:
            axes[c].set_ylabel(f"Channel {c+1}")
    figure.suptitle("waveform")
    plt.show()

def plot_specgram(waveform, sample_rate, title="Spectrogram"):
    waveform = waveform.numpy()

    num_channels, num_frames = waveform.shape

    figure, axes = plt.subplots(num_channels, 1)
    if num_channels == 1:
        axes = [axes]
    for c in range(num_channels):
        axes[c].specgram(waveform[c], Fs=sample_rate)
        if num_channels > 1:
            axes[c].set_ylabel(f"Channel {c+1}")
    figure.suptitle(title)
    plt.show()

plot_waveform(sample[0], SAMPLING_FREQUENCY)
plot_specgram(sample[0], SAMPLING_FREQUENCY)

# Save audio sample
output_dir = os.path.dirname(__file__)
filename = os.path.join(output_dir, 'sample.wav')
torchaudio.save(filename, sample[0], SAMPLING_FREQUENCY)