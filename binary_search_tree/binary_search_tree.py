"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
          if self.left is None:
            self.left = BSTNode(value)
            return # OPTIONAL
          else:
            return self.left.insert(value)
        elif value >= self.value:
          if self.right is None:
            self.right = BSTNode(value)
            return # OPTIONAL
          else:
            return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
      if self.value == target:
        return True
      if target < self.value:
        if self.left is None:
          return False
        return self.left.contains(target)
      if target > self.value:
        if self.right is None:
          return False
        return self.right.contains(target)

    # Return the maximum value found in the tree
    # INTERATIVE
    def get_max2(self):
      cur_node = self
      max_value = self.value
      while cur_node.right is not None:
        cur_node = cur_node.right
        max_value = cur_node.value
      return max_value

    # RECURSIVE
    def get_max(self):
      if not self.right:
        return self.value
      return self.right.get_max()

    # RECURSIVE

    def for_each(self, fn):
      fn(self.value)
      if self.left is not None:
        self.left.for_each(fn)
      if self.right is not None:
        self.right.for_each(fn)
      return

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
      if node:
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def dft_print(self, node):
      stack = []
      stack.append(self)
      while len(stack) > 0:
        current = stack.pop()
        if current.right:
          stack.append(current.right)
        if current.left:
          stack.append(current.left)
        print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def bft_print(self, node):
      queue = deque()
      queue.append(self)
      while len(queue) > 0:
        current = queue.popleft()
        if current.left:
          queue.append(current.left)
        if current.right:
          queue.append(current.right)
        print(current.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BSTNode(5)
# bst.insert(30)
# max_val = bst.get_max()
# print("Max: " + str(max_val))
# # should print 30 but prints None



bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.in_order_print(bst)
bst.bft_print(bst)
bst.dft_print(bst)
#     # ITERATIVE
# import random
# v1 = random.randint(1, 101)
# v2 = random.randint(1, 101)
# v3 = random.randint(1, 101)
# v4 = random.randint(1, 101)
# v5 = random.randint(1, 101)

# bst1 = BSTNode(5)
# bst1.insert(2)
# bst1.insert(1)
# bst1.insert(4)
# bst1.insert(5)
# bst1.insert(3)

# bst1.in_order_print(bst1)
# bst1.for_each(lambda v: print("for_each: " + str(v)))
# bst1.interative_for_each(lambda v: print("interative_for_each: " + str(v)))
# bst1.interative_for_each_using_queue(lambda v: print("interative_for_each_using_queue: " + str(v)))

#so breadth/iterate for queues and depth/recursion for stacks?

# research breadth-first vs depth-first