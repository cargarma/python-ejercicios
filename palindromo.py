# Definir una función es_palindromo() para reconocer palíndromos

def reverso(cadena):
	resultado = ""
	for letra in cadena:
		resultado = letra + resultado
	return resultado

def es_palindromo(palabra):
	 return reverso(palabra) == palabra


def es_palindromo_v2(palabra):
	palabra2 = palabra
	for letra in palabra:
		if palabra2[-1] == letra:
			palabra2 = palabra2[:-1]
		else:
			return False

	if len(palabra2) == 0:
		return True
	else:
		return False

print(es_palindromo("radar"))
print(es_palindromo_v2("radar"))

print(es_palindromo("sradar"))
print(es_palindromo_v2("ra ar"))
