#!/usr/bin/env python
# -*- coding: utf-8 -*-

print
print
print    "---------------------------LICEO COMPU-MARKET---------------------------------"
print    "----------------------------4TO. BACO SEC. C----------------------------------"
print    "------------------------------PROGRAMACION------------------------------------"
print    "------------------PROFESOR ERICK ALBERTO GONZALEZ CRUZ------------------------"
print    
print    "_______________________________________________________________________________"
print    "-------------------------------INTEGRANTES:------------------------------------"
print
print     "                   1. --- Seiddy Gabriela Roca Lemus"
print     "                   2. --- Elizabeth Andrea Sagche"
print
print
print
print
print
print
print
print

#declaramos la lista como global
global lista
lista = list()

#Creamos una clase llama PaisyC
class Paisyc:
	pais = ""
	capital = ""

#funcion Registrarpais, para poder ingresar y guardar los datos
def registrarpais():
	print u"Registrar País y Capital"
	
#creamos objeto p.
	p = Paisyc()

	p.pais = raw_input ("Ingrese pais")
	p.capital = raw_input("Ingrese capital")

#añadimos los objetos a la lista
	lista.append(p)

#funcion Listapais, para mostrar el listado de los datos almacenados.
def listapais():
	print "Listado de paises y capitales"

#ciclo for para recorrer la lista y mostrar datos.
	for p in lista:
		print p.pais, "-", p.capital


def salir():
	print u"Gracias por utilizar la aplicación"

#se crea la funcion menu
def menu():
	op = 0

#siclo while.
	while op !=3:
		# mostrar el menu
		print u"----------Menú de opciones-----------"
		print u"1. Registrar nombre de país y capital"
		print u"2. Enlistar países y capitales"
		print "3. Salir"
		op = raw_input("Digita una opción: ")

#se crea una condicion para llamar funciones.
		if op == 1:
			registrarpais()
		elif op == 2:
			listapais()
		elif op == 3:
			salir()  

#se llama a la funcion menu.
menu()
