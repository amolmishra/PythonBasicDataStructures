class EmptyQueueError(Exception):
    """
        Custom Error for Empty Queue.

    """

    pass


class Queue:
    """
        Queue: FIFO Data Structure
        Operations:
            enQueue(item)
            dequeue()
            peek()
            isEmpty()
            size()
    """

    def __init__(self):
        """
            Define an Empty Queue
            Using list to define a queue
        """
        self._data = []     # Holding items in queue

    def isEmpty(self):
        """
            Test if queue has no items
            :return true if queue is empty, false otherwise
        """

        return self.size() == 0

    def enQueue(self, item):
        """
            Adds an Item to the top of the Queue and updates the top
        :param item: item to be added on top
        """
        self._data.append(item)

    def dequeue(self):
        """
            Removes an item from top of the queue, modifying it
        :return: The item on top of the queue
        :raises: EmptyQueueError if queue has no elements
        """
        if self.isEmpty():
            raise EmptyQueueError("Queue is Empty: Trying to dequeue from an empty queue.")

        return self._data.pop(0)

    def size(self):
        """
            Returns the number of elements currently in the queue
        :return: The size of the queue
        """
        return len(self._data)


if __name__ == "__main__":
    s = Queue()

    s.enQueue("Hello")
    s.enQueue("World")

    print("Size of the queue is {}.".format(s.size()))

    while not s.isEmpty():
        print(s.dequeue())

    import time
    time.sleep(5)           # To ensure that the output from program and exception is not interleaved.

    # try to dequeue from an empty queue

    s.dequeue()

    time.sleep(1)
    print("Done!!!")
