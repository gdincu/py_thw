import sys
import time
while True:
  for i in ["/","-","|","\\","|"]:
    sys.stdout.write("%s\r" % i)
    sys.stdout.flush()
    time.sleep(.05)
    
#Print in one line dynamically
"""
tempName = str(input("Nume: "))
for i in range(0,len(tempName),1):
  print(tempName[i], sep=' ', end='', flush=True)
"""

#Return a list of the words in a string, using sep as the delimiter string. 
"""
def citeste():
  temp = str(input("Value: "))
  tempValues = temp.split(sep=" ", maxsplit=-1)
  for i in tempValues:
    print(i)
"""

