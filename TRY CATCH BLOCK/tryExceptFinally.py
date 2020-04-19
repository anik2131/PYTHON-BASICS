try: # exception to be handled
  number1=int(input("Enter first number: "))
  number2=int(input("Enter second number: "))
  print(number1/number2)
except ValueError:
  print("Invalid input")
except ZeroDivisionError:  #Exception caught
  print("Divide by Zero Error")
finally: # it is always executed irrespective of try-except block
  print("Try-Except Block executed Successfully")
