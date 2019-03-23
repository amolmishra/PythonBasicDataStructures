class Node:
    """
        A class representing a node in binary tree
    """

    def __init__(self, data):
        """
            Define a node in the binary tree
        :param data: the data or payload that the node holds
        """
        self._data = data
        self._right = None
        self._left = None

    def insert_left(self, data):
        """
            Insert a node as left child of the node
        :param data: payload for the left child
        :return: none
        """
        node = Node(data)

        if self.get_left_child() is None:
            self.set_left_child(node)
        else:
            node._left = self.get_left_child()
            self.set_left_child(node)

    def insert_right(self, data):
        """
            Insert a node as right child of the node
        :param data: payload for the right child
        :return: None
        """
        node = Node(data)

        if self.get_right_child() is None:
            self.set_right_child(node)
        else:
            node._right = self.get_right_child
            self.set_right_child(node)

    def get_left_child(self):
        """
        Get the left child of the node
        :return: The left child of the node
        """
        return self._left

    def get_right_child(self):
        """
        Get the right child of the node
        :return: The right child of the node
        """
        return self._right

    def set_right_child(self, new_node):
        """
        Set the right child of the node
        :param new_node to be set as the right child
        :return: None
        """
        self._right = new_node

    def set_left_child(self, new_node):
        """
        Set the left child of the node
        :param new_node: node to be set as the left child
        :return: None
        """
        self._left = new_node

    def get_data(self):
        """
        get the data from the node
        :return: data/payload of the node
        """
        return self._data


class BinaryTree:
    """
    A class representing a binary tree
    """
    def __init__(self, data):
        """
        Initializing the tree with a root holding some data
        :param data: The data/payload of the root node
        """
        self._root = Node(data)

    def get_root(self):
        """
        Get the root of the tree
        :return: The root node of the tree
        """
        return self._root

    def _in_order(self, node):
        if node is None:
            return

        self._in_order(node.get_left_child())
        print(node.get_data())
        self._in_order(node.get_right_child())

    def in_order(self):
        """
        Traverse the tree using in order traversal method
        :return: None
        """
        self._in_order(self.get_root())


if __name__ == "__main__":

    """
                                5
                               / \
                              /   \
                             /     \
                            3       7
                           / \     / \
                          /   \   /   \
                         2     4 6
    """

    t = BinaryTree(5)

    t.get_root().insert_left(3)
    t.get_root().insert_right(7)

    left_child = t.get_root().get_left_child()
    left_child.insert_right(4)
    left_child.insert_left(2)

    right_child = t.get_root().get_right_child()
    right_child.insert_left(6)
    t.in_order()
