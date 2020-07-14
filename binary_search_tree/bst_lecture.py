# LEFT child value less than parent value
# RIGHT child value is greater (or equal if dups are allowed) than parent value

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        pass

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
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

bst = BSTNode(20)
bst.left = BSTNode(10)
bst.right = BSTNode(34)
bst.left.left = BSTNode(4)
bst.left.right = BSTNode(19)
bst.right.left = BSTNode(21)
bst.right.right = BSTNode(100)

print(bst.contains(20))
print(bst.contains(10))
print(bst.contains(34))
print(bst.contains(4))
print(bst.contains(19))
print(bst.contains(21))
print(bst.contains(100))