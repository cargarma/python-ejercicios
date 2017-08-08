#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dias_de_la_semana=["lunes",
					"martes", 
					"miércoles", 
					"jueves",
					"viernes",
					"sabado",
					"domingo", True, "lunes"]


print(dias_de_la_semana)
print(dias_de_la_semana[0])
print(dias_de_la_semana[-1]) # Valores negativos para empezar desde el final
print(dias_de_la_semana[1:2])
print(dias_de_la_semana[:2]) # Entiende que comienza desde 0
print(dias_de_la_semana[2:]) # Hasta el final

# Añadir elemento al final
dias_de_la_semana.append("monday")

#Añadir elemento en una posición 
dias_de_la_semana.insert(3,"tuesday")

#Añadir varios elementos
dias_de_la_semana.extend(["wednesday", "friday"])

# Índice de un elemento
print(dias_de_la_semana.index("lunes"))

# Comprobar si contiene un elemento
print("lunes" in dias_de_la_semana)


# Eliminar elemento por valor
# Repetido elimina el primero
# Error si no existe
dias_de_la_semana.remove("lunes")
dias_de_la_semana.remove("lunes")

days_week = ["sunday, thursday"]


# Unir listas
print(dias_de_la_semana+days_week)

print("lunes" in dias_de_la_semana)


