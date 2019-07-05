"""""""""""""""""""""""""""""""""""""""""""""""""""
TCP client
"""""""""""""""""""""""""""""""""""""""""""""""""""
import socket
import sys

#Uses the ip as a username
userName = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

#Creating a listening socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Connecting to the socket
s.connect(("127.0.0.1",7777))

try:	
	#Sending data
	noteToSend = input("[%s]: " % userName)
	s.send("%s,%s".encode() % (userName.encode(),noteToSend.encode()))

	if(noteToSend ==  ("exit")):
		sys.exit(0)

	#Printing the received data
	b=s.recv(140)
	print("[%s]: %s" % (b.decode().split(",")[0],b.decode().split(",")[1]))
except:
	# Recreate the socket and reconnect
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(("127.0.0.1",7777))