"""
    Testing out PyTorch 2.0 Functionality.

    https://pytorch.org/get-started/pytorch-2.0/#pytorch-2x-faster-more-pythonic-and-as-dynamic-as-ever

"""

import torch
import time
import torch.nn.functional as F

print("PyTorch Version: ", torch.__version__)
print("Is CUDA available: ", torch.cuda.is_available())
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


for device in [
    torch.device("cpu"),
    torch.device("cuda"),
    ]:
    print("Device: ", device)

    weight = torch.randn(3, 3, 3, 3).to(device)
    bias = torch.randn(3).to(device)
    bn_mean = torch.randn(3).to(device)
    bn_var = torch.randn(3).to(device)

    @torch.compile
    def model(x):
        # if time.time() % 2 == 0:
        #     x = F.conv2d(x, weight, bias)
        x = F.conv2d(x, weight, bias)
        x = F.batch_norm(x, bn_mean, bn_var)
        x = F.relu(x)
        return x

    foo_input = torch.randn(1, 3, 28, 28).to(device)

    # Run foo_conv once to compile the graph
    start_time = time.time()
    output = model(foo_input)
    original_time = time.time() - start_time
    print("Run model with no compilation: ", original_time)

    # Run foo_conv again to measure the execution time
    start_time = time.time()
    output = model(foo_input)
    eager_time = time.time() - start_time
    print("Run model after eager compilation: ", eager_time)
    print("Eager speedup: ", original_time / eager_time)

    compiled_model = torch.compile(
        model,
        dynamic=True,
        # ['dynamo_minifier_backend', 'dynamo_accuracy_minifier_backend', 'cudagraphs', 'eager', 'ts', 'aot_eager', 'aot_eager_decomp_partition', 'aot_ts', 'inductor', 'ipex', 'nvprims_nvfuser', 'nvprims_aten', 'aot_ts_nvfuser', 'onnxrt', 'torchxla_trivial', 'torchxla_trace_once', 'aot_torchxla_trivial', 'aot_torchxla_trace_once', 'tvm']
        backend="eager",
        fullgraph=True,
    )
    output = compiled_model(foo_input)

    # Run foo_conv again to measure the execution time
    start_time = time.time()
    output = compiled_model(foo_input)
    compiled_time = time.time() - start_time
    print("Run model after torch.compile: ", compiled_time)
    print("Compiled speedup: ", original_time / compiled_time)

    foo_input = torch.randn(1, 3, 32, 32).to(device)

    # Run foo_conv again to measure the execution time
    start_time = time.time()
    output = model(foo_input)
    dynamic_shape_time = time.time() - start_time
    print("Model after dynamic shape: ", dynamic_shape_time)
    print("Dynamic Shape Speedup: ", original_time / dynamic_shape_time)

