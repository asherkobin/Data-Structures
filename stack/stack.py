"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
#from .. doubly_linked_list.doubly_linked_list import DoublyLinkedList
import sys
sys.path.append("../singly_linked_list")
from singly_linked_list import LinkedList, Node

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        if self.storage.head == None:
          self.storage.head = Node(value)
          self.storage.tail = self.storage.head
        else:
          old_head = self.storage.head
          self.storage.head = Node(value)
          self.storage.head.next = old_head
        self.storage.length += 1
    
    def pop(self):
        if self.storage.head == None:
          return None
        item_to_remove = self.storage.head
        self.storage.head = self.storage.head.next
        self.storage.length -= 1
        return item_to_remove.value
