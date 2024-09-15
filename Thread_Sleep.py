from time import sleep
from threading import Thread
import numpy as np

def task(sleep_time, message):
    print('----------NEW THREAD_______ : NEW THREAD STARTED EXECUTION')
    #block for a moment
    sleep(sleep_time)
    #display a mssg
    print("----------NEW THREAD_______" ,"Thread Completed it's job")

def main():
    # create a thread
    thread = Thread(target=task, args=(1, "Thread Completed it's job"))
    print("----------MAIN THREAD---------- : STARTED A NEW THREAD")

    # run the thread
    thread.start()
    print("---------------MAIN THREAD------------------- : Main thread continues and computed the rad")
    radius = 2
    area = np.pi * radius ** 2
    print("----------MAIN THREAD---------- : AREA OF A CIRCLE", area)
    print("-----------MAIN THREAD---------- : Waiting foe the new thread to complete before exiting")
    print('All thread completed ! ! ! ')
    thread.join()

if __name__ == "__main__":
    main()