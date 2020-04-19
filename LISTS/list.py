L=[ 0 , 1 , 2 , 3 , 4 ]

print(L) # print the whole list [ 0 , 1 , 2 , 3 , 4 ]

for i in L: # print each element in the list in a new line
  print(i)

print("The length of the list is: "+str(len(L))) # return the size of the list

L.append(69) # append the data at the end of the list
print(L) # [ 0 , 1 , 2 , 3 , 4 , 69 ]

L.pop(3) # pops and returns the number at index 3
print(L)

L.pop(-2) # pops and returns the second last element from the list
print(L)

L.remove(2) # removes the number "2" from the list if it is present
print(L)

L.clear() # Remove all items from the list
print(L)

l=list(range(10)) # insert values from 0 - 9
del l[2:8:2] # [start:stop:step] deletes values from 2-7 increamenting by 2 steps / positions
print(l)

l.sort(reverse=True) # sort the lists in reverse order (Descending)
print(l)

a= [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
for n, i in enumerate(a):
      if i == 1:
         a[n] = 10  # replace the value 1 by value 10 in list "a"
print(a)

a[5]=100   # replace the value at index 5 with value "100"
print(a)

# --------OUTPUT--------
#[0, 1, 2, 3, 4]
#0
#1
#2
#3
#4
#The length of the list is: 5
#[0, 1, 2, 3, 4, 69]
#[0, 1, 2, 4, 69]
#[0, 1, 2, 69]
#[0, 1, 69]
#[]
#[0, 1, 3, 5, 7, 8, 9]
#[9, 8, 7, 5, 3, 1, 0]
#[10, 2, 3, 4, 5, 10, 2, 3, 4, 5, 10]
#[10, 2, 3, 4, 5, 100, 2, 3, 4, 5,10]