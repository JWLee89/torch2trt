from torch2trt.torch2trt import *
from torch2trt.module_test import add_module_test


def convert_cast(ctx):
    """
    A simple converter for supporting casting operations.

    IMPORTANT: Note that because TensorRT does not support
    64 bit data types, .long() will not be supported
    """
    input_tensor = ctx.method_args[0]
    layer = ctx.network.add_identity(input_tensor._trt)
    output = ctx.method_return
    output._trt = layer.get_output(0)


@tensorrt_converter("torch.float")
@tensorrt_converter("torch.Tensor.float")
def convert_float(ctx):
    convert_cast(ctx)


@tensorrt_converter("torch.bool")
@tensorrt_converter("torch.Tensor.bool")
def convert_bool(ctx):
    convert_cast(ctx)


@tensorrt_converter("torch.float")
@tensorrt_converter("torch.Tensor.float")
def convert_bool(ctx):
    convert_cast(ctx)
