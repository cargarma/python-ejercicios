#Funcion sum() y multip() que sumen y multipliquen respectivamente todos los números de una lista. 

def sum(lista):
	if not lista:
	   return 
	else:
		resultado = 0
		for elemento in lista:
			resultado += elemento
		return resultado

def multip(lista):
	if not lista:
	   return 
	else: 
		resultado = 1
		for elemento in lista:
			resultado *= elemento
		return resultado



print(sum([1,6,4,4]))
print(sum([1,6,8,4]))
print(sum([1,6,8,-4]))
print(sum([1,6,8,True]))
print(sum([]))

print(multip([1,6,8,4]))
print(multip([1,6,8,0]))
print(multip([1,6,8,-1]))
print(multip([]))