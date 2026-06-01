# join方法的作用是阻塞当前进程，等join前面的进程执行完，再继续往下执行

import os
import time
from multiprocessing import Process, current_process, RLock


def speek(*a):
    lock = a[1]
    lock.acquire()
    # 使用with lock会自动加锁、自动释放锁
    with lock:
        for i in range(10):
            print("好", end="")
            print("好", end="")
            print("学", end="")
            print("习", end="")
            print("天", end="")
            print("天", end="")
            print("向", end="")
            print("上")
            time.sleep(1)
        # lock.release()


def study():
    for i in range(15):
        print("A", end="")
        print("B", end="")
        print("C", end="")
        print("D")
        time.sleep(1)


if __name__ == '__main__':
    # 使用Process类创建进程对象
    print('开始执行')
    lock = RLock()
    p1 = Process(target=speek, name="p1", args=(1, lock))
    p2 = Process(target=study, name="p2")
    p1.start()
    # join方法在start之后再执行才可以
    # join传递参数为等待时间
    p1.join(5)
    p2.start()
    # p2.join()
    print('结束执行')
