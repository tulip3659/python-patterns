"""
This is a simple file to practice a few ideas in queues. A good website with simple examples:
https://dbader.org/blog/queues-in-python

"""

import queue

q = queue.Queue()

q.put("Babak")
q.put(60)

for _ in range(5):
    # It doesn't raise exception Empty in python 3.5
    print(q.get())
