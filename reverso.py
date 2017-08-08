#Definir una función reverso() que calcule el reverso de una cadena.

def reverso(cadena):
	resultado = ""
	for letra in cadena:
		resultado = letra + resultado
	return resultado
	
print(reverso("Hola"))
print(reverso("Estoy probando el reverso"))