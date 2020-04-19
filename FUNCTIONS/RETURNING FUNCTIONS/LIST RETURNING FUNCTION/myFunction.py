# FIRST SEE THE PROGRAMS OF THE LISTS

def myFunction(x):
  return list( dict.fromkeys(x))

mylist = myFunction([1,2,3,4,5,1,2,3,4,6,7,8,9])
print(mylist) 