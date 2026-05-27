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
        # lock.release()
        time.sleep(1)


def study():
    for i in range(15):
        print("A", end="")
        print("B", end="")
        print("C", end="")
        print("D")
        time.sleep(1)


if __name__ == '__main__':
    # 使用Process类创建进程对象
    lock = RLock()
    p1 = Process(target=speek, name="p1", args=(1, lock))
    p2 = Process(target=study, name="p2")
    p1.start()
    p2.start()
