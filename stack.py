class EmptyStackError(Exception):
    """
        Custom Error for Empty BasicDS.

    """

    pass


class Stack:
    """
        BasicDS: LIFO Data Structure
        Operations:
            push(item)
            pop()
            peek()
            isEmpty()
            size()
    """

    def __init__(self):
        """
            Define an Empty BasicDS
            Using list to define a stack
        """
        self._list = []     # Holding items in stack
        self._top = -1      # denotes the top index of stack

    def isempty(self):
        """
            Test if stack has no items
            :return true if stack is empty, false otherwise
        """

        return self._top == -1

    def push(self, item):
        """
            Adds an Item to the top of the BasicDS and updates the top
        :param item: item to be added on top
        """
        self._list.append(item)
        self._top += 1

    def pop(self):
        """
            Removes an item from top of the stack, modifying it
        :return: The item on top of the stack
        :raises: EmptyStackError if stack has no elements
        """
        if self.isempty():
            raise EmptyStackError("BasicDS is Empty: Trying to pop from an empty stack.")

        self._top -= 1
        return self._list.pop()

    def peek(self):
        """
            Returns the top of stack without modifying it
        :return:  The top of stack
        :raises:  EmpytyStackError if stack has no elements
        """

        if self.isempty():
            raise EmptyStackError("BasicDS is Empty: Trying to peek into an empty stack.")

        return self._list[self._top]

    def size(self):
        """
            Returns the number of elements currently in the stack
        :return: The size of the stack
        """
        return self._top + 1


if __name__ == "__main__":
    s = Stack()

    s.push("Hello")
    s.push("World")

    print("Size of the stack is {}. The element on top is {}".format(s.size(), s.peek()))

    while not s.isempty():
        print(s.pop())

    import time
    time.sleep(5)           # To ensure that the output from program and exception is not interleaved.

    # try to pop from an empty stack

    s.pop()

    time.sleep(1)
    print("Done!!!")
