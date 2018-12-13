"""
This file is intended to practice pool design pattern. The link below was useful in understanding the python context manager
https://jeffknupp.com/blog/2016/03/07/improve-your-python-the-with-statement-and-context-managers/

DISCLAIMER: I am not sure if this is the best practice of pool pattern as I am not trying to access the pool simultaneously.

"""

import queue, time

class Expensive_class():

    def __init__(self, build_time):
        self._build_time = build_time
        print("Beginning the build")
        time.sleep(self._build_time)
        print("Building ended!")

    def use(self):
        print("Using the object")
        time.sleep(0.3)

class Object_pool():

    def __init__(self, queue):
        self._queue = queue
        self._item = None

    def __enter__(self):
        if self._item is None:
            self._item = self._queue.get()
        return self._item

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._item is not None:
            self._queue.put(self._item)
            self._item = None

if __name__=="__main__":
    # This section shows how it works without pool design pattern
    t = time.time()
    for _ in range(3):
        obj = Expensive_class(1)
        obj.use()
    delta_t = time.time() - t
    print('Time elapsed with individual objects: {}'.format(delta_t))

    # This section shows how it works with pool design pattern
    q = queue.Queue()
    q.put(Expensive_class(1))

    t = time.time()
    with Object_pool(q) as pool:
        for _ in range(3):
            pool.use()

    delta_t = time.time() - t
    print('Time elapsed with pool design pattern: {}'.format(delta_t))