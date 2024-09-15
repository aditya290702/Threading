from time import sleep
from threading import Thread
import numpy as np

def task(sleep_time, message):
    print('-----NEW THREAD----- : NEW THREAD STARTED EXECUTION')
    #block for a moment
    sleep(sleep_time)
    #display a mssg
    print("-----NEW THREAD FOR THE FINAL MESSAGE-----" ,message)

def main():
    # create a thread
    thread = Thread(target=task, args=(5, "Thread Completed it's job"))
    print("-----MAIN THREAD----- : STARTED A NEW THREAD")

    # run the thread
    thread.start()
    print("-----MAIN THREAD----- : Main thread continues and computed the rad")
    radius = 2
    area = np.pi * radius ** 2
    height = 10
    base = 5
    areaT = 0.5*base*height
    print("-----MAIN THREAD----- : AREA OF A CIRCLE", area)
    print("-----MAIN THREAD----- : Waiting foe the new thread to complete before exiting")
    print("-----MAIN THREAD----- : AREA OF A TRIANGLE", areaT)
    print("                ")
    print('All thread completed ! ! ! ')
    thread.join()

if __name__ == "__main__":
    main()