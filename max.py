#Funciones que devuelven la mayor valor de los pasados por parámetro

def max_de_dos(numero1, numero2):
	if numero1 > numero2:
		return numero1
	else:
		return numero2


def max_de_tres(numero1, numero2, numero3):
	if numero1 > numero2:
		if numero1 > numero3:
			return numero1
		else:
			return numero3
	else:
		if numero2 > numero3:
			return numero2
		else:
			return numero3


def max_de_tres_v2(numero1, numero2, numero3):
	if numero1 > numero2 and numero1 > numero3:		
		return numero1
	else:
		if numero2 > numero3:
			return numero2
		else:
			return numero3



# Calcula recursivamente el máximo de una lista de elementos
def max_lista(lista):
	if len(lista) == 0:
	   return 
	elif len(lista) == 1:
		return lista[0]
	else:
		maximo = max_lista(lista[1:])
		if lista[0] > maximo:
			return lista[0] 
		else:
			return maximo	


#Pruebas


print(max_de_dos(1,4))
print(max_de_tres(1,4,4))
print(max_de_tres_v2(1,4,7))

lista = [1,4,4]
print(max_lista(lista))
lista = [27,28,26,4,2,9,4,-1,32]
print(max_lista(lista))
lista = []
print(max_lista(lista))
lista = [27,28,26,4,2,9,True,-1,32]
print(max_lista(lista))