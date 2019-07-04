import sys

def scade(a,b):
	return a-b

def aduna(a,b):
	return a+b
	
def inmulteste(a,b):
	return a*b
	
def imparte(a,b):
	return a/b
	
def switch(operatia,nrUnu,nrDoi):
	if(operatia == "scade" or operatia == "Scade"): 
		print(scade(nrUnu,nrDoi))
	if(operatia == "aduna" or operatia == "Aduna"): 
		print(aduna(nrUnu,nrDoi))
	if(operatia == "inmulteste" or operatia == "Inmulteste"):
		print(inmulteste(nrUnu,nrDoi))
	if(operatia == "imparte" or operatia == "Imparte"):
		print(imparte(nrUnu,nrDoi))
	
nrUnu = int(input("Alege primul numar: "))
nrDoi = int(input("Alege al doilea numar: "))
operatia = input("Alege operatia (scade/ aduna/ inmulteste/ imparte): ")
switch(operatia,nrUnu,nrDoi)

sys.exit(0)