def longitud(elemento):
	contador = 0
	for i in elemento:
		contador += 1
	return contador

def longitud_recursiva(elemento):
	if  not elemento:
		return 0
	else:
		return 1+ longitud_recursiva(elemento[1:])
	


#Pruebas
cadena = "ABCDEFG"
cadena_vacia = ""

lista = ["casa", "coche","avión"]

print(longitud(cadena))
print(longitud_recursiva(cadena))

print(longitud(cadena_vacia))
print(longitud_recursiva(cadena_vacia))

print(longitud(lista))
print(longitud_recursiva(lista))
