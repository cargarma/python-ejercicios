#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Utilización de IF
print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Introduce la nota del alumno:")

def evaluacion(nota):
	if nota < 0 or nota > 10:
	   return "Error en la nota"
	else:
		valoracion="aprobado"
		if nota<5:
			valoracion="suspenso"
		return valoracion


print(evaluacion(int(nota_alumno)))