#UDP server in Python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.bind(("0.0.0.0",5555))                           
buff,addr=s.recvfrom(10)                           
print buff
s.sendto("hello", addr)                        

#UDP client in Python
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.sendto("hey",("127.0.0.1",5555))                 
print s.recvfrom(10) 