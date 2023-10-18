import threading
import time


# 多线程操作
# 1.创建多线程
def run1(n):
    print("thread1 start!")
    time.sleep(n)
    print(f"loop {n}s, thread1 finish!")


def run2(n):
    print("thread2 start!")
    time.sleep(n)
    print(f"loop {n}s, thread2 finish!")


# 2. 绑定多线程，可传参
thread1 = threading.Thread(target=run1, args=(4,))
thread2 = threading.Thread(target=run2, args=(2,))


# # 3. 守护线程
# thread2.daemon = True
thread1.start()
thread2.start()


print("all thread finish")

# 3. 异常处理

