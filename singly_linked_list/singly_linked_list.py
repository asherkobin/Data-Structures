class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def contains(self, value):
        result = False
        cur = self.head
        while cur != None:
          if cur.value == value:
            result = True
            break
          cur = cur.next
        return result

    def get_max(self):
        max = None
        cur = self.head
        while cur != None:
          if cur.value > max:
            max = cur.value
          cur = cur.next
        return max

    def add_to_tail(self, value):
      new_node = Node(value)
      if self.head == None:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node 
        self.tail = new_node
      self.length += 1

    def remove_head(self):
      if self.head == None:
        return None
      else:
        if self.head == self.tail:
          self.tail = None
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value