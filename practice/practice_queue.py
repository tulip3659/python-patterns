"""
This is a simple file to practice a few ideas in queues. A good website with simple examples:
https://dbader.org/blog/queues-in-python

"""

import queue

# q = queue.Queue()
#
# q.put("Babak")
# q.put(60)
#
# for _ in range(5):
#     # It doesn't raise exception Empty in python 3.5
#     print(q.get())


class Sample_Class():
    """
    Sample class to see if you can put objects in a queue
    """
    def __str__(self):
        return "Object!"


qq = queue.Queue()

obj1 = Sample_Class()
obj2 = Sample_Class()

qq.put(obj1)
qq.put(obj2)
print(qq.qsize())
print(qq.get())
print(qq.qsize())

