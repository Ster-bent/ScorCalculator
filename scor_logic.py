value = int(input())
operator = str(input())
value2 = int(input())

def addition(value,value2):
  print(value+value2)
  return

def subtraction(value,value2):
  print(value-value2)
  return

def multiplication(value,value2):
  print(value*value2)
  return

def division(value,value2):
  print(value/value2)
  return

def exponent(value,value2):
  print(value**value2)
  return

#actual logic
while True:
  if operator == '+':
    addition(value,value2)
  elif operator == '-':
    subtraction(value,value2)
  elif operator == '*':
    multiplication(value,value2)
  elif operator == '/':
    division(value,value2)
  elif operator == '^':
    exponent(value,value2)
  else:
    print('invalid operation')
  print('operation complete')
  sigfig = str(input())
  if sigfig == 'sigfigm':
    print('placeholder')
  elif sigfig == 'cancel':
    break
