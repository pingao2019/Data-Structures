#doubly_linked_list.py

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
    the old head node's previous pointer accordingly.""


  def add_to_head(self, value):
    new_head = ListNode(value,None,self.head)
    if self.head == None and self.tail == None:
      self.head = new_head
      self.tail = new_head
      self.head.prev = None
      self.head.next = None
      self.length = 1
    else:
      self.head.prev = new_head
      new_head.prev = None
      self.head = new_head
      self.length += 1
  

  """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

  def remove_from_head(self):
    removed = self.head.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.head = self.head.next
      self.head.prev.delete()
      self.length -= 1
    return removed
  

  """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""


  def add_to_tail(self, value):
    new_tail = ListNode(value, self.tail)
    if self.head == None and self.tail == None:
      self.head = new_tail
      self.tail = new_tail
      self.head.prev = None
      self.head.next = None
      self.length = 1
    else:
      self.tail.next = new_tail
      self.tail = new_tail
      self.length += 1
  
  """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""


  def remove_from_tail(self):
    removed = self.tail.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.tail = self.head.prev
      self.tail.next.delete()
      self.length -= 1
    return removed
  

  """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

  def move_to_front(self, node):
    self.add_to_head(node.value)
    self.length -= 1

  """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

  def move_to_end(self, node):
    if self.length > 1 and node != self.tail:
      self.tail.insert_after(node.value)
      self.tail = self.tail.next
    if node == self.head: 
      self.head = node.next
    node.delete()
  
  """Removes a node from the list and handles cases where
    the node was the head or the tail"""

  def delete(self, node):
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    elif self.tail == node:
      self.remove_from_tail()
    elif self.head == node:
      self.remove_from_head()
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
      self.length -= 1


    """Returns the highest value currently in the list"""
    
  def get_max(self):
    max_val = -float("inf")
    location = self.head
    while location != None:
      if location.value > max_val:
        max_val = location.value
      location = location.next
    return max_val