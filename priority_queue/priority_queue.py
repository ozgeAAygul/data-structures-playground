from Heap import Heap

class PriorityQueue:
  def __init__(self):
    self.heap = Heap()

  def enqueue(self, e):
    self.heap.insert(e)
  
  def dequeue(self):
    if self.is_empty():
      return None
    return self.heap.extract_min()
  
  def peek(self):
    if self.is_empty():
      return None
    return self.heap.get_min()
  
  def getSize(self):
    return self.heap.size()
  
  def is_empty(self):
    return self.heap.is_empty()
