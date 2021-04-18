'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder
than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node


class AVLTree():
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in
    the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that
        all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        if node and AVLTree._balance_factor(node) in [-1, 0, 1]:
            if node.left and node.right:
                return AVLTree._is_avl_satisfied(node.left)\
                    and AVLTree._is_avl_satisfied(node.right)
            if node.left and node.right is None:
                return AVLTree._is_avl_satisfied(node.left)
            if node.right and node.left is None:
                return AVLTree._is_avl_satisfied(node.right)
        return True

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level
        overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree
        code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.right is None:
            return node

        new_node = Node(node.right.value)
        new_node.right = node.right.right
        new_left = Node(node.value)
        new_left.left = node.left
        new_left.right = node.right.left

        new_node.left = new_left
        return new_node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level
        overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is
        fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.left is None:
            return node

        new_node = Node(node.left.value)
        new_node.left = node.left.left
        new_right = Node(node.value)
        new_right.right = node.right
        new_right.left = node.left.right
        new_node.right = new_right
        return new_node

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview
        of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree
        code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code
        for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(value, self.root)

    def insert_list(self, xs):
        for i in xs:
            self.insert(i)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
            else:
                return AVLTree._right_rotate(node)

        elif AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
            else:
                return AVLTree._left_rotate(node)

        else:
            return node

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                AVLTree._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                AVLTree._insert(value, node.right)

        if AVLTree._is_avl_satisfied(node) is False:
            node.left = AVLTree.rebalance(node.left)
            node.right = AVLTree.rebalance(node.right)
            return AVLTree.rebalance(node)
        else:
            return node
