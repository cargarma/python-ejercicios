#Comprobador vocales: Dado un carácter, devuelve True si es una vocal, en caso contrario devuelve False.

def es_vocal(elemento):
  #Comprueba tipo str
	if isinstance(elemento, str) :
		vocales = 'aáãâàäeéèêëiíìiîïoóòõôöuúùûü'
		return elemento.lower() in vocales			
	else:
		return False



#Pruebas

print(es_vocal('A'))
print(es_vocal('É'))
print(es_vocal('Z'))
print(es_vocal('0'))
print(es_vocal(-1))
print(es_vocal('a'))
print(es_vocal('ú'))