from linked_list import LinkedList

class Stack:
  def __init__(self):
    self.__list = LinkedList()
  
  def isEmpty(self):
    return self.__list.isEmpty()
  
  def push(self, e):
    self.__list.addFirst(e)
  
  def pop(self):
    return self.__list.removeFirst()

  def peek(self):
    return self.__list.first()

  def __len__(self):
    return self.__list.__len__()

  def __str__(self):
    elements = []
    current = self.__list._LinkedList__head
    while current:
      elements.append(str(current.element))
      current = current.next
    
    return "Top ->" + "->".join(elements)

  
