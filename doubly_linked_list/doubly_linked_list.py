"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
      ln = ListNode(value)
      ln.next = self.head
      if self.head != None:
        self.head.prev = ln
      self.head = ln
      if self.tail == None:
        self.tail = ln
      self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
      if self.length == 0:
        return None
      removed_head = self.head
      if self.head == self.tail:
        self.head = None
        self.tail = None
      else:
        self.head = removed_head.next
      self.length -= 1
      return removed_head.value

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
      if self.length == 0:
        return None
      removed_tail = self.tail
      if self.head == self.tail:
        self.head = None
        self.tail = None
      else:
        self.tail = removed_tail.prev
      self.length -= 1
      return removed_tail.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
      ln = ListNode(value)
      ln.prev = self.tail
      if self.tail != None:
        self.tail.next = ln
      self.tail = ln
      if self.head == None:
        self.head = ln
      self.length += 1

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
      node.delete()
      if node == self.tail:
        self.tail = node.prev
      self.head.prev = node
      node.next = self.head
      node.prev = None
      self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
      node.delete()
      if node == self.head:
        self.head = node.next
      self.tail.next = node
      node.next = None
      node.prev = self.tail
      self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
      if self.head == node:
        self.head = self.head.next
      if self.tail == node:
        self.tail = self.tail.prev
      else:
        node.delete()
      self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
      cur_node = self.head
      highest_value = 0
      while True:
        if cur_node.value > highest_value:
          highest_value = cur_node.value
        cur_node = cur_node.next
        if cur_node == None:
          break
      return highest_value

