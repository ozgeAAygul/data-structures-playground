class Empty(Exception):
  pass

class Node:
  def __init__(self, element):
    self.element = element
    self.next = None 
  
class LinkedList:
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0
  
  # BASIC METHODS

  def __len__(self):
    return self.__size
  
  def isEmpty(self):
    return self.__size == 0

  def first(self):
      if self.isEmpty():
          raise Empty("List is empty")
      return self.__head.element
  
  # ADD METHODS
  
  def addFirst(self, e):
    new = Node(e)
    if self.isEmpty():
      self.__head = self.__tail = new
    else:
      new.next = self.__head
      self.__head = new
    self.__size += 1
  
  def addLast(self, e):
    new = Node(e)
    if self.isEmpty() :
      self.__head = self.__tail = new
    else:
      self.__tail.next = new
      new.next = None
      self.__tail = new
    self.__size += 1
  
  def insert(self, index, e):
    if index < 0 or index > self.__size:
      raise IndexError("Index out of bounds")
    
    if index == 0:
      self.addFirst(e)
    elif index == self.__size:
      self.addLast(e)
    else:
      current = self.__head
      for i in range(index - 1):
        current = current.next

      new = Node(e)
      new.next = current.next
      current.next = new

      self.__size += 1
    
  # REMOVE METHODS

  def removeFirst(self):
    if self.isEmpty():
      raise Empty("List is Empty")
    
    current = self.__head
    self.__head = self.__head.next
    self.__size -=1

    return current.element
  
  def removeLast(self):
    if self.isEmpty():
      raise Empty("List is Empty")
    
    if self.__size == 1:
      temp = self.__head
      self.__head = self.__tail = None
      self.__size = 0
      return temp.element
    
    current = self.__head
    for i in range(self.__size - 2):
      current = current.next
    
    temp = self.__tail
    current.next = None
    self.__tail = current
    self.__size -= 1

    return temp.element
  
  def remove(self, index):
    if index < 0 or index >= self.__size:
      raise IndexError("Index out of bounds")
    
    if index == 0:
      return self.removeFirst()
    elif index == self.__size - 1 :
      return self.removeLast()
    else:
      current = self.__head
      for i in range(index - 1):
        current = current.next

      temp = current.next
      current.next = temp.next
      self.__size -= 1

      return temp.element
    
  # ITERATION & PRINT
  
  def __iter__(self):
    current = self.__head
    while current:
      yield current.element
      current = current.next
  
  def __str__(self):
    return " -> ".join(str(x) for x in self)
  

