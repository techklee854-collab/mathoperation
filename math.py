try:
  a = float(input("Enter first number: "))
  b = float(input("enter second number: "))
  print(f"Addition:{a+b}")
  print(f"Subtraction:{a-b}")
  print(f"Multuiplication:{a*b}")
  if b != 0:
    print(f"Divison:{a/b}")
  else:
    print("Division by zero not possible")  
except ValueError:
  print(f"Enter valid numbers..")
  
