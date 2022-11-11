import subprocess
import torch
from huggingface_hub import snapshot_download
from torch.utils.data import DataLoader

from foldingdiff import modelling
from foldingdiff import datasets

model = modelling.BertForDiffusion.from_dir(
    snapshot_download("wukevin/foldingdiff_cath"))

# # Load dataset (we might not need this for inference)
# clean_data = datasets.CathCanonicalAnglesOnlyDataset(
#     pad=128, trim_strategy='randomcrop')
# noisy_data = datasets.NoisedAnglesDataset(
#     clean_data, timesteps=1000, beta_schedule='cosine')
# loader = DataLoader(noisy_data, batch_size=32, shuffle=False)

# # Get a single data point for inference
# x = iter(loader).next()
# predicted_noise = model(x['corrupted'], x['t'], x['attn_mask'])

# Get device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Size of generated protein (number of residues)
min_len: int = 32 # 50
max_len: int = 34 # 128

num_samples_per_length: int = 1 #10
batch_size = 8 #512

# Generate a protein by sampling from model
subprocess.run([
    "python",
    "/home/tren/dev/foldingdiff/bin/sample.py",
    "-l", f"{min_len}", f"{max_len}",
    "-n", f"{num_samples_per_length}",
    "-b", f"{batch_size}",
    "--device",  f"{device}",
    "-o", "/tmp/foldingdiff",
    "--seed", "42",
])

