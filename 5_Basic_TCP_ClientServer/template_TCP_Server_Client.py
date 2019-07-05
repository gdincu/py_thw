#TCP server in Python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(5)
cs,addr=s.accept()
b=cs.recv(10)
print b
cs.send("Hello")
cs.close()

#TCP client in Python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",7777))
s.send("Salut")
print s.recv(10)
s.close()

#TCP multithreaded server in Python
import time
import socket
from threading import Thread
def f(cs,i):
 print ("Procesez client"+str(i))
 b=cs.recv(10)
 time.sleep(10)
 cs.send(str(i))
 cs.close()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(5)
i=0
while (1==1):
 i=i+1
 cs,addr=s.accept()
 t=Thread(target=f,args=(cs,i,))
 t.start()