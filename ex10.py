import sys
import time
while True:
  for i in ["/","-","|","\\","|"]:
    sys.stdout.write("%s\r" % i)
    sys.stdout.flush()
    time.sleep(.05)