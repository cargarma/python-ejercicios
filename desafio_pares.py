#Dado un vector de enteros, debes encontrar el suma de los elementos en posición par y multiplicar la suma por el último elemento de la lista.

def suma_pares(numeros):
	if numeros: 
		return sum(numeros[0::2]) * numeros[-1]
	else:
		return 0


print(suma_pares([]))
print(suma_pares([12,34,2,-1,4,7]))