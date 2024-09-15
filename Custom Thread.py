from time import sleep
from threading import Thread

import numpy as np


class CustomThread(Thread):
    def run(self):
        # create a thread
        print("----------NEW THREAD IS COMING---------- : CREATING A NEW THREAD")
        sleep(5)
        radius = 5
        self.area = np.pi * radius**2
        print("-----MAIN THREAD----: DONE")

def main():
    thread = CustomThread()
    print("----MSIN THREAD---- : CREATING A NEW ONE")
    thread.start()
    print("-----WAITING FOE FINISHING---------")
    thread.join()
    area_Circle = thread.area
    print(f"---MAIN THREAD----- Area for circle computed in a thread : {area_Circle}")

if __name__ == "__main__":
    main()