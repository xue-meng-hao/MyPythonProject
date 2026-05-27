import os
import time
from multiprocessing import Process, current_process,Lock


def speek(a,msg):
    for i in range(10):
        print(f"说话函数：{i},进程pid:{os.getpid()},父进程ppid:{os.getppid()},进程名:{current_process().name},参数:{a},{msg}")
        time.sleep(1)


def study():
    for i in range(15):
        print(f"学习函数：{i},进程pid:{os.getpid()},父进程ppid:{os.getppid()},进程名:{current_process().name}")
        time.sleep(1)


if __name__ == '__main__':
    # 使用Process类创建进程对象
    p1 = Process(target=speek, name="p1",args=(1,),kwargs={"msg":"值"})
    p2 = Process(target=study, name="p2")
    p1.start()
    p2.start()

# Process的参数：
# group：进程组，默认None,始终为None
# target:紫禁城要执行的可调用对象，默认为None
# name:进程名称，默认为None
# args:传递给目标函数的位置参数，默认为空元祖
# kwargs:传递给目标函数的关键字参数字典，默认为空字典
# daemon:是否是守护进程，默认为False
