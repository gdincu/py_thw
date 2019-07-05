"""""""""""""""""""""""""""""""""""""""""""""""""""
TCP server 
- returns the month of a year
- logs requests & replies into a Log txt file
"""""""""""""""""""""""""""""""""""""""""""""""""""
import socket
import sys
from datetime import datetime

#Function to return answers based on Client input
def sMessage(inputMessage): 
    switcher = { 
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
		"": "Try again"
    } 
    return switcher.get(inputMessage, "Invalid month. Needs to be between 1 - 12")

#Uses the ip as a username
userName = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

#Records all messages into a Log txt file. If this doesn't exist it gets created automatically
f = open('LogConvers.txt',"a+")

#Records into the log file a new session
currTime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
f.write('\n{:70s}'.format('==================================================================='))
f.write('\n{:20s} | {:20s} | {:30s}'.format('Sender','Date & Time','Message'))
f.write('\n{:70s}\n'.format('==================================================================='))

#Creating a listening socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))	

#To be shown while server is running
print('Server running ...')

while True:		
	s.listen(140)
	cs,addr=s.accept()
	b=cs.recv(140)
	
	#Writes the date & time of request & User request to server into the Log file
	currTime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	f.write('{:20s} | {:20s} | {:30s}\n'.format(b.decode().split(",")[0],currTime, b.decode().split(",")[1]))	
	
	try:
		val = int(b.decode().split(",")[1])
		MsgToSend = sMessage(b.decode().split(",")[1])
		cs.send("%s,%s".encode() % (userName.encode(),MsgToSend.encode()))
		#Date & Time of sending the reply & the actual reply
		currTime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		f.write('{:20s} | {:20s} | {:30s}\n'.format('[Server]: ',currTime, MsgToSend))
	except ValueError:
		#If 'exit' is received the server shuts down
		if b.decode().split(",")[1] == "exit":
			print('Server stopped')
			sys.exit(0)
		cs.send("%s,%s".encode() % (userName.encode(),'Not a number - Try again'.encode()))
		#Date & Time of sending the reply & the actual reply
		currTime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		f.write('{:20s} | {:20s} | {:30s}\n'.format('[Server]: ',currTime, 'Not a number - Try again'))