'''
This file implements the Heap data structure
as a subclass of the BinaryTree.
The book implements Heaps using an *implicit*
tree with an *explicit* vector implementation,
so the code in the book is likely to be less
helpful than the code for the other data structures.
The book's implementation is the traditional
implementation because it has a faster constant factor
(but the same asymptotics).
This homework is using an explicit tree implementation
to help you get more practice with OOP-style
programming and classes.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass
    of BinaryTree.
    You should make the necessary changes in the
    class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be
        inserted into the Heap.
        '''
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a
        string that can be used to recreate a
        valid instance of the class.
        Thus, if you create a variable using the
        command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be
        the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses
        of Heap will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a
        function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test
        whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        if node is None or (node.left is None and node.right is None):
            return True

        elif node.right is None:
            return node.value <= node.left.value

        elif node.value <= node.left.value and node.value <= node.right.value:
            a = Heap._is_heap_satisfied(node.left)
            b = Heap._is_heap_satisfied(node.right)
            return a and b

        else:
            return False

    def insert(self, value):
        '''
        Inserts value into the heap.

        FIXME:
        Implement this function.

        HINT:
        The pseudo code is
        1. Find the next position in the tree using
        the binary representation of the total number of nodes
            1. You will have to explicitly store the
            size of your heap in a variable (rather than
            compute it) to maintain the O(log n) runtime
            1. See https://stackoverflow.com/questions/18241192/
            implement-heap-using-a-binary-tree for hints
        1. Add `value` into the next position
        1. Recursively swap value with its parent until
        the heap property is satisfied

        HINT:
        Create a @staticmethod helper function,
        following the same pattern used in the
        BST and AVLTree insert functions.
        '''
        if self.root:
            self.root = Heap._insert(self.root, value)
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1

    @staticmethod
    def _insert(node, value):
        if node is None:
            return
        if node.left and node.right:
            node.left = Heap._insert(node.left, value)
            if node.value > node.left.value:
                return Heap._up(node, value)
        if node.left is None:
            node.left = Node(value)
            if node.value > node.left.value:
                return Heap._up(node, value)
        elif node.right is None:
            node.right = Node(value)
            if node.value > node.right.value:
                return Heap._up(node, value)
        return node

    @staticmethod
    def _up(node, value):
        if Heap._is_heap_satisfied(node) is True:
            return node
        if node.left and node.left.value > node.value:
            node.left = Heap._up(node.left, value)
        if node.right and node.right.value > node.value:
            node.right = Heap._up(node.right, value)
        if node.left:
            if node.left.value == value:
                new_parent = node.left.value
                new_left = node.value
                node.value = new_parent
                node.left.value = new_left
        if node.right:
            if node.right.value == value:
                new_parent = node.right.value
                new_right = node.value
                node.value = new_parent
                node.right.value = new_right

        return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element
        of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        return self.root.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        The pseudocode is
        1. remove the bottom right node from the tree
        2. replace the root node with what was
        formerly the bottom right
        3. "trickle down" the root node: recursively swap
        it with its largest child until the heap
        property is satisfied

        HINT:
        I created two @staticmethod helper functions:
        _remove_bottom_right and _trickle.
        It's possible to do it with only a
        single helper (or no helper at all),
        but I personally found dividing up the
        code into two made the most sense.
        '''
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            replace_right = Heap._rightmove(self.root)
            self.root = Heap._remove(self.root)
            if replace_right == self.root.value:
                return
            else:
                self.root.value = replace_right
            if Heap._is_heap_satisfied(self.root) is False:
                return Heap._down(self.root)

    @staticmethod
    def _remove(node):
        if node is None:
            return
        elif node.right:
            node.right = Heap._remove(node.right)
        elif node.left:
            node.left = Heap._remove(node.left)
        else:
            if node.right is None and node.left is None:
                return None
        return node

    @staticmethod
    def _rightmove(node):
        if node.left is None and node.right is None:
            return node.value
        elif node.right:
            return Heap._rightmove(node.right)
        elif node.left:
            return Heap._rightmove(node.left)

    @staticmethod
    def _down(node):
        if node.left is None and node.right is None:
            return node
        if node.left and (node.right is None or node.left.value <= node.right.value):
            if node.left.value < node.value:
                new_parent = node.left.value
                new_left = node.value
                node.value = new_parent
                node.left.value = new_left
            node.left = Heap._down(node.left)
        elif node.right and (node.left is None or node.right.value <= node.left.value):
            if node.right.value < node.value:
                new_parent = node.right.value
                new_right = node.value
                node.value = new_parent
                node.right.value = new_right
            node.right = Heap._down(node.right)
        return node
