import tensorrt as trt
import pycuda.autoinit  # 负责内存管理，数据初始化
import pycuda.driver as cuda  # gpu, cpu数据传输


# 1. creat logger
logger = trt.Logger(trt.Logger.ERROR)
# 2. create builder
builder = trt.Builder(logger)
# 3. create runtime
runtime = trt.Runtime(logger)
# 4. read engine and deserialize
with open("sample_yolov5s.engine", "rb") as f:
    engine = runtime.deserialize_cuda_engine(f.read())
    host_inputs = []
    cuda_inputs = []
    host_outputs = []
    cuda_outputs = []
    for binding in engine:
        size = trt.volume(engine.get_binding_shape(binding)) * 1
        dims = engine.get_binding_shape(binding)
        print(size)
        print(dims)
        print(binding)
        print(engine.binding_is_input(binding))
        dtype = trt.nptype(engine.get_binding_dtype(binding))
        print("dtype = ", dtype, "\n")
# 5. buffer准备host, device
        host_mem = cuda.pagelocked_empty(size, dtype)
        cuda_mem = cuda.mem_alloc(host_mem.nbytes)
        if engine.binding_is_input(binding):
            pass







