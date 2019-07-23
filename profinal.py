#!/usr/bin/env python
# -*- coding: utf-8 -*-

print
print
print    "---------------------------LICEO COMPU-MARKET---------------------------------"
print    "----------------------------4TO. BACO SEC. C----------------------------------"
print    "------------------------------PROGRAMACION------------------------------------"
print    "------------------PROFESOR ERICK ALBERTO GONZALEZ CRUZ------------------------"
print
print
print    
print    "_______________________________________________________________________________"
print    "-------------------------------INTEGRANTES:------------------------------------"
print
print     "                   1. --- Seiddy Gabriela Roca Lemus"
print     "                   2. --- Elizabeth Andrea Sagche"


#declaramos la lista como global
global lista
lista = list()

#Creamos una clase llama PaisyC
class PaisyC:
	Pais = ""
	Capital = ""

#funcion Registrarpais, para poder ingresar y guardar los datos.
def Registrarpais():
	print u"Registrar País"

#creamos objeto p.
	p = PaisyC()

	p.Pais = raw_input (u"Ingrese país")
	p.Capital = raw_input("Ingrese capital")

#añadimos los objetos a la lista.
	lista.append(p)

#funcion Listapais, para mostrar el listado de los datos almacenados.
def Listapais():
	print "Listado de paises y capitales"

#ciclo for para recorrer la lista y mostrar datos.
	for p in lista:
		print p.Pais, "-", p.Capital

def buscar():
	print u"Buscar un país o capital"

	Pais = raw_input("Ingrese el pais a buscar: ")

	for p in lista:
		if p.Pais == Pais:
			print p.Pais, "-", p.Capital

def salir():
	print u"Gracias por utilizar la aplicación"


def menu():
	op = 0

	while op !=4:
		print u"Menú"
		print u"1. Registrar nombre de país y capital"
		print u"2. Enlistar países y capitales"
		print u"3. Buscar País o capital"
		print "4. Salir"
		op= raw_input ("Elige una opción: ")

		if op == 1:
			Registrarpais()
		elif op == 2:
			Listapais()
		elif op == 3:
			buscar()
		elif op == 4:
			salir()


menu()


