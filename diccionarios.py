#Inicialización
midiccionario = {23:"Jordan", "nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993]}}

#Añadir elemento
midiccionario["Posición"] = "Escolta"

#Borrar 
del midiccionario["Equipo"]

#Listar claves
print(midiccionario.keys())

#listar valores
print(midiccionario.values())

#Longitud diccionario
print(len(midiccionario))

print(midiccionario)