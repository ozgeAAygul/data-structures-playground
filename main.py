from evaluator import evaluate

def main():
  expr = input("Enter expression: ")
  try: 
    result = evaluate(expr)
    print("Result:", result)
  except:
    print("Invalid expression")

main()