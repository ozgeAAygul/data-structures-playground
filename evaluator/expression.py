def insert_blanks(s):
  result = ""
  for ch in s:
    if ch in "()+-*/":
      result += " " + ch + " "
    else:
      result += ch
  return result

from stack import Stack

def evaluate(expression):
  operandStack = Stack()
  operatorStack = Stack()

  expression = insert_blanks(expression)
  tokens = expression.split()

  for token in tokens:
    if token.replace(".", "", 1).isdigit(): #sadece ilk noktayı silmesini istediğimizden en sona 1 yazdık
      operandStack.push(float(token))

    elif token in "+-":
      while (not operatorStack.isEmpty() and operatorStack.peek() in "+-*/"):
        process(operandStack, operatorStack)
      operatorStack.push(token)

    elif token in "*/":
      while (not operatorStack.isEmpty() and operatorStack.peek() in "*/"):
        process(operandStack, operatorStack)
      operatorStack.push(token)
    
    elif token == "(":
      operatorStack.push(token)
    
    elif token == ")":
      while operatorStack.peek() != "(":
        process(operandStack, operatorStack)
      operatorStack.pop()
    
  while not operatorStack.isEmpty():
    process(operandStack, operatorStack)
    
  return operandStack.pop()

def process(operandStack, operatorStack):
  op = operatorStack.pop()

  b = operandStack.pop()
  a = operandStack.pop()

  if op == "+":
    operandStack.push(a + b)
  elif op == "-":
    operandStack.push(a - b)
  elif op == "*":
    operandStack.push(a * b)
  elif op == "/":
    operandStack.push(a / b)

