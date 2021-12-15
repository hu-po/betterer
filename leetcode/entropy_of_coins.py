import torch

x = torch.rand(3)
print(f'x {x}')

# Is the inverse probability different/faster than the of interpretation?
probability = x / torch.sum(x)
print(f'probability {probability}')

sur_entropy = torch.sum(probability*torch.log(1/probability))
print(f'entropy from suprise {sur_entropy}')
og_entropy = -torch.sum(probability*torch.log(probability))
print(f'entropy OG formula {og_entropy}')

# How does the entropy compare for different coins?
p_faircoin = torch.tensor([0.5, 0.5])
p_unfaircoin = torch.tensor([0.7, 0.3])
p_haineouscoin = torch.tensor([0.99, 0.01])
faircoin_og_entropy = -torch.sum(p_faircoin*torch.log(p_faircoin))
unfaircoin_og_entropy = -torch.sum(p_unfaircoin*torch.log(p_unfaircoin))
haineouscoin_og_entropy = -torch.sum(p_haineouscoin*torch.log(p_haineouscoin))
print(f'faircoin entropy OG formula {faircoin_og_entropy}')
print(f'unfaircoin entropy OG formula {unfaircoin_og_entropy}')
print(f'haineouscoin entropy OG formula {haineouscoin_og_entropy}')
