import asyncio
import os

# 1. 使用协程的方式调用CMD程序，并返回标准输出和标准错误
async def run():
    '''
    :return: stdout, stderr
    '''
    process = await asyncio.create_subprocess_exec("python3", "Tensorrt/01_hello_tensorrt.py", stdout=asyncio.subprocess.PIPE)
    print(process)

    stdout, stderr = await process.communicate()
    print(stdout)
    return stdout, stderr
asyncio.run(run())

# 2. 获取进程ID


