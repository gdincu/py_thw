from sys

print("The script name is: ",sys.argv[0])

print("Nr of arguments: ",len(sys.argv))

print("The arguments are: ",str(sys.argv))

if len(sys.argv) > 1:
	for i in range(1,len(sys.argv),1):
		print("Argument %d: " %i,sys.argv[i])