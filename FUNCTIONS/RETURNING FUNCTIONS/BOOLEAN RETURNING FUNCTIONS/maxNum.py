def maximumNumber(a,b):
  if(a>b):
    return True
  else:
    return False

a=input("Enter the first number: ")
b=input("Enter the second number: ")

if(maximumNumber(float(a),float(b))):
  print(a+" is greater than "+b)
else:
  print(b+" is greater than "+a)
