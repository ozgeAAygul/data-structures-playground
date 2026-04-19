class Empty(Exception):
  pass

"""Circular Queue"""
class ArrayQueue:
  DEFAULT_CAPACITY = 5

  def __init__(self):
    self.__data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self.__size = 0
    self.__front = 0
  
  def __len__(self):
    return self.__size
  
  def is_empty(self):
    return self.__size == 0
  
  def first(self):
    if self.is_empty():
      raise Empty("Queue is Empty")
    return self.__data[self.__front]

  def dequeue(self):
    if self.is_empty():
      raise Empty("Queue is Empty")

    temp = self.__data[self.__front]
    self.__data[self.__front] = None
    self.__front = (self.__front + 1) % len(self.__data)
    self.__size -= 1
    return temp
  
  def enqueue(self, e):
    if self.__size == len(self.__data):
      self.__resize(2*len(self.__data))
    avail = (self.__front + self.__size) % len(self.__data)
    self.__data[avail] = e
    self.__size += 1

  def __resize(self, cap):
    old = self.__data
    self.__data = [None] * cap
    walk = self.__front
    for i in range(self.__size):
      self.__data[i] = old[walk]
      walk = (1 + walk) % len(old)
    self.__front = 0
  
  def __str__(self):
    result = []
    walk = self.__front
    for _ in range(self.__size):
        result.append(str(self.__data[walk]))
        walk = (walk + 1) % len(self.__data)
    return "< " + " ".join(result) + " <"