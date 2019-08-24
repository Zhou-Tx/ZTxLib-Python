from threading import Thread


# As one thread
class MyThread(Thread):
    def __init__(self,
                 name,          # thread_name
                 function,      # function_name
                 queue):        # queue_name
        Thread.__init__(self)
        self.__name__ = name
        self.__queue__ = queue
        self.__function__ = function

    def run(self):
        # print(self.name + " starts")
        while True:
            try:
                self.__function__(self.__queue__)
            except:
                break
        # print(self.name + " ends")


class MyThreads:
    def __init__(self, function, queue):
        self.__function__ = function
        self.__queue__ = queue

    def start(self, count=5):  # join为是否阻塞
        threads = []
        threadings = []
        for i in range(count):
            threads.append("thread-"+str(i))
        for tName in threads:
            thread = MyThread(tName, self.__function__, self.__queue__)
            thread.start()
            threadings.append(thread)
        for t in threadings:
            t.join()


# Demo
def demo():
    # Define a function
    def func(q):
        data = q.get(timeout=1)
        try:
            print(data + 1)
        except:
            pass
    print('-Start-')
    # Define a queue for data
    from queue import Queue
    queue = Queue()
    for i in range(99):
        queue.put(i)
    # define threads an start it
    threads = MyThreads(func, queue)
    threads.start()
    # End
    print('-End-')


if __name__ == "__main__":
    demo()
