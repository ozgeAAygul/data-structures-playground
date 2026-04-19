class Empty(Exception):
  pass

class Node:
  def __init__(self, element):
    self.element = element
    self.next = None 

class LinkedStack:
  def __init__(self):
    self.__head = None
    self.__size = 0
  
  def __len__(self):
    return self.__size
  
  def is_empty(self):
    return self.__size == 0
  
  """
  def top(self):
    if self.is_empty():
      raise Empty("Stack is Empty")
    else:
      return self.__head.element
  """
#daha doru versiyonu var

  def peek(self):
    if self.is_empty():
      raise Empty("Stack is Empty")
    return self.__head.element

  def push(self, e):
    new = Node(e)
    new.next = self.__head
    self.__head = new
    self.__size += 1
  
  def pop(self):
    if self.is_empty():
      raise Empty("Stack is Empty")
    node = self.__head
    self.__head = node.next
    self.__size -= 1
    return node.element
  
  def __iter__(self):
      current = self.__head
      while current:
          yield current.element
          current = current.next
          
  def __str__(self):
    return " -> ".join(str(x) for x in self)