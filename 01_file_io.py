import json
import xml
import shutil
import os


# 文件查询、创建、拷贝、删除
# 1.查询
path = "01_file_io.py"
if os.path.exists(path):
    print(f"{path}文件存在")
# 2.创建与删除
#   a) 单文件夹创建
os.mkdir("01_file_io/")
#   b) 单文件夹删除
#os.rmdir("01_file_io/")
#   c) 递归文件夹夹创建
os.makedirs("01_file_io/test")
#   d) 递归文件夹夹删除
#os.removedirs("01_file_io/test")
# 3. 拷贝
shutil.copy("01_file_io.py", "01_file_io_dist.py")