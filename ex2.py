#################################################################
"""
4 collection data types in Python
- Lists - collection which is ordered and changeable. Allows duplicates.
- Tuple - collection which is ordered and unchangeable. Allows duplicates.
- Set	- collection which is unordered and unindexed. No duplicate members.
- Dictionary - collection which is unordered, changeable and indexed. No duplicate members.
"""
#################################################################

#Lists
"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist[1])

for x in thislist:
	print(x)
  
if "apple" in thislist:
	print("apple")
	
print len(thislist)

thislist.append("orange")
print(thislist)

thislist.insert(0, "orange")
print(thislist)

thislist.remove("orange")
print(thislist)

thislist.pop()
print(thislist)

thislist.pop(1)
print(thislist)

del thislist[0]
print(thislist)

del thislist

#copy a list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)
"""

#Tuples
"""
tempTuple = ("cherry","apple","banana")
print(tempTuple[1])

for x in tempTuple:
  print(x)
  
if "apple" in tempTuple:
	print("Yes, 'apple' is in the fruits tuple")
	
x = tempTuple.index('apple')
print(x)
"""

#Sets
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)
"""

#Dictionaries
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
"""

#If...Else
"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
if a > b or a > c:
  print("At least one of the conditions is True")
"""

#While Loops
"""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
"""

#For Loops
"""
for x in "banana":
  print(x)
  
for x in range(2, 6):
  print(x)
  
for x in range(2, 30, 3):
  print(x)
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)  
"""

#Functions
"""
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function()

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Recursive functions
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""