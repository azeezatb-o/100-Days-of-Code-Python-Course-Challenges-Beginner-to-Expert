from art import logo
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

operations = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
  go_on = True
  while go_on:
    operation_symbol = input("Pick an operation: ")
    num = float(input("What is the next number?: "))
    calculate = operations[operation_symbol]
    answer = calculate(num1, num)
    print(f"{num1} {operation_symbol} {num} = {answer}")
    decide = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
    if decide == 'n':
      go_on = False
      calculator()
    elif decide == 'y':
      num1 = answer
    else:
      print("Type a valid response")

calculator()