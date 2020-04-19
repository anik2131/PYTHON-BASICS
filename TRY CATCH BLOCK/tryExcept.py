try:
  number1=int(input("Enter first number: "))
  number2=int(input("Enter second number: "))
  print(number1/number2)
except ValueError:
  print("Invalid input")
except ZeroDivisionError:
  print("Divide by Zero Error")