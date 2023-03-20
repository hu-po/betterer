import torch
import torchvision
import random
import time
import torchvision.models as models
import tensorboard

print("PyTorch Version: ", torch.__version__)
print("TorchVision Version: ", torchvision.__version__)
print("Is CUDA available: ", torch.cuda.is_available())
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

for device in [
    torch.device("cpu"),
    torch.device("cuda"),
    ]:
    print("\nDevice: ", device)
    
    for compile_mode in [
        "reduce-overhead",
        "max-autotune",
    ]:
        print("\nCompile mode: ", compile_mode)
        model = models.vit_b_16().to(device)
        optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
        compiled_model = torch.compile(
            model,
            backend="eager",
            mode=compile_mode,
            # fullgraph=True,
            dynamic=True,
            # static_graph=True,
        )
        torch.save(compiled_model.state_dict(), "compiled.model.pt")
        # both these lines of code do the same thing
        torch.save(model.state_dict(), "model.pt")

        for i in range(8):
            start_time = time.time()
            if i < 2:
                x = torch.randn(16, 3, 224, 224).to(device)
            else:
                batch_size = random.randint(14, 18)
                print(f"Random batch size: {batch_size}")
                x = torch.randn(batch_size, 3, 224, 224).to(device)
            optimizer.zero_grad()
            out = compiled_model(x)
            out.sum().backward()
            optimizer.step()
            total_time = time.time() - start_time
            print(f"Fake epoch {i} took {total_time} seconds")