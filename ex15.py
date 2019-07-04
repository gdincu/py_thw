from sys
filename = sys.argv[1]
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Read a File
'r' is the default mode. It opens a file for reading and reads the entire content of the file.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
f=open(filename, "r")
if f.mode == 'r':
	contents =f.read()
print(contents)

#readlines - used to read the contents of a file line by line
fTemp = f.readlines()
for x in fTemp:
	print(x)
	
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Adds to the file
'w' opens the file for writing. If the file doesn't exist it creates a new file. If the file exists it truncates the file.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
f= open("template.txt","w+")
print("Adds lines to the file: ")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
	 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Create a new file
'x'	creates a new file. If the file already exists, the operation fails.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
f= open("newFile.txt",x)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Append Data to a File
'a' opens a file in append mode. If the file does not exist, it creates a new file
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
f=open(filename, "a+")	
for i in range(2):
     f.write("Appended line %d\r\n" % (i+1))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Truncate a file
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Opens the file & provides writing permission
print("Opening the file....")
txt = open(filename,'w+')
#Truncates the file
print("Truncating the file")
target.truncate()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Close a file
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
target.close()