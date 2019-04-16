import threading
import os, time


def square(num):
    print("PID of square thread is {}".format(str(os.getpid())))
    print("Name of square thread is {}".format(threading.current_thread().name))
    print(num*num)


def cube(num):
    print("PID of cube thread is {}".format(str(os.getpid())))
    print("Name of cube thread is {}".format(threading.current_thread().name))
    time.sleep(5)
    print(num*num*num)



if __name__ == '__main__':

    print ("Starting main thread {} with PID {}".format(threading.main_thread().name,os.getpid()))

    t1 = threading.Thread(target=square, args=(10,), name='thread_sq')
    t2 = threading.Thread(target=cube, args=(10,), name='thread_cube')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print ("I am done!!")
