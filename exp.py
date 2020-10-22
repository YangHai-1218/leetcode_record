import threading
import time


def display(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name, "------", time.time())

class Mythread(threading.Thread):
    def __init__(self, name, delay):
        super(Mythread, self).__init__()
        self.delay = delay
        self.name = name
    
    def run(self):
        print('start run')
        display(self.name, self.delay)
        print('end run')


thread1 = Mythread('tom', 1)
thread1.start()
thread1.join()