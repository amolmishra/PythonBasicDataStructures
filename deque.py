class EmptyDequeueError(Exception):
    """
        Custom Error for Empty Dequeue.

    """

    pass


class Dequeue:
    """
        Dequeue: neither LIFO nor FIFO Data Structure
        Operations:
            addFront(item)
            addRear(item)
            removeFront()
            removeRear()
            isEmpty()
            size()
    """
