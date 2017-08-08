tupla_ej = (1, "Casa", 2341) # Parentesis opcionales
print(tupla_ej[1])

# Comprobar si elemento existe
print(2341 in tupla_ej)

#  Cuantas veces aparece
print(tupla_ej.count("Casa"))


# Convertir tupla en lista
lista = list(tupla_ej)

#Convertir lista en tupla
mitupla = tuple(lista)


#Longitud de tupla
print(len(tupla_ej))

print(tupla_ej)

#desempaquetado de tupla

cantidad, lugar, cp = tupla_ej
print(cantidad)


#Las tuplas no se pueden modificar