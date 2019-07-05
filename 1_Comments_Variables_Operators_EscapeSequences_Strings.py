#one-line comment
"""
multi
line
comment
"""

#Functions
"""
def prints(a,b,c):
  print(a)
  print(b)
  print(c)
"""
  
#Variables
"""
x,y,z = 2,3,'Name'
prints(x,y,z)
z=15
print("z's values is " + str(z))
z='15'
print("x+y+z = " + str((x+y+int(z))))
x=y=z
prints(x,y,z)
print("X would be %d, Y is %s and Z is %r" %(x, str(y), z))
"""

#Numbers
"""
import random
print(random.randrange(1,10))

x = 1 # int
#convert from int to float:
a = float(x)

y = 2.8 # float
#convert from float to int:
b = int(y)

z = 2j # complex
#convert from int to complex:
c = complex(x)
"""

#Strings
'''
multiLineString = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiLineString)
'''

"""
multiLineString = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,'''
print(multiLineString)
"""

"""
b = "Hello, World!"
print(b[2:5])
print(b.strip())
print(len(b))
print(b.lower())
print(b.upper())
print(b.replace("H","J"))
print(b.split(",")[1])

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
"""

#Formatter
"""
formatter = "%r %d %s"
print (formatter % (1,2,'3'))
"""

#Operators
"""
print(5%3)
print(5**2)
print(5//2) #rounds down the result of the division
print(5==5)
x = 3
print not(x < 5 and x < 10)
print (x is 3)
print (x is not 3)
x = ["apple", "banana"]
print("pineapple" not in x)
"""

#Escape sequences
"""
\\ -> \
\' -> '
\" -> "
\a -> ASCII bell -> Bell character is an ASCII control character, code 7 (^G). When it is sent to a printer or a terminal, nothing is printed, but an audible signal is emitted instead. You can emit a beep by printing the ASCII Bell character ("\0007") to the console.
\b -> Backspace
\f -> formfeed
\n -> linefeed
\N{name} -> char named name in the unicode database
\r -> carriage return
\t -> horizontal tab
\uxxx -> char with 16-bit hex value xxxx
\Uxxxxxxxx -> char with 32-bit hex value xxxxxxxx
\v -> vertical tab
\ooo -> char with octal value ooo
\xhh -> char with hex value hh
"""
