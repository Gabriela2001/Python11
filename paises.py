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
print    
print 	    "______________________________________________________________________________"
print  	    "|--------------------------INTEGRANTES:---------------------------------------|"
print 	    "|                                                                             |"   
print 	    "|                   1. --- Seiddy Gabriela Roca Lemus                         |"
print 	    "|                   2. --- Elizabeth Andrea Sagche                            |"
print 	    "|                   3. --- Karla Pamela Vasquez Castellano                    |"
print 	    "|                   4. --- Cesar Daniel Tello Guzman                          |"
print 	    "|                   5. --- Tiffanie Aracely Solis Sanchez                     |"
print  	    "|_____________________________________________________________________________|"
print
print
print

#declaramos la lista como global
global lista
listap = []
lista = []

#funcion a, para poder ingresar y guardar los datos
def a():

	print
	print
	print  "--------------------------------------------------------------------------------"
	print u"                       REGISTRO DE PAISES Y CAPITALES     "
	print  
	print "__________________________________|"
	pais = raw_input("|      Ingrese Pais:  ")
	print "|                                 |"
	capital = raw_input("|      Ingrese Capital: ")
	print "|_________________________________|"
	print
	print
	print "	|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
	print "		           SE HAN ALMACENADO LOS DATOS."
	print "	|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
	print
	print "---------------------------------------------------------------------------------"


	listap.append(pais)
	lista.append(capital)

#funcion Listapais, para mostrar el listado de los datos almacenados.
def listapais():

	print
	print
	print  "---------------------------------------------------------------------------------"
	print  "	                  LISTADO DE PAISES Y CAPITALES      "
	print 
	print
	print
	print "PAIS:    " + str(listap) 
	print "CAPITAL: " + str(lista) 
	print
	print  "---------------------------------------------------------------------------------"


def salir():
	print
	print
	print  "--------------------------------------------------------------------------------"
	print  "	               GRACIAS POR UTILIZAR ESTA APLICACION.                        "
	print  "--------------------------------------------------------------------------------"

#se crea la funcion menu
def menu():
	op = 0

#siclo while
	while op !=3:
		# mostrar el menu
		print
		print
		print
		print u"		-----------------Menú----------------------"
		print  "		|                                         |"
		print u"		| 1.- Registrar nombre de país y capital  |"
		print u"		| 2.- listar países y capitales           |"
		print  "		| 3.- Salir                               |"
		print  "		|                                         |"
		print  "		-------------------------------------------"
		print
		print
		print "|---------------------------------------|"
		op = input("	 Digita una opcion: ")     
		print "|---------------------------------------|"
#se crea una condicion para llamar funciones.		
		if op == 1:
			a()
		elif op == 2:
			listapais()
		elif op == 3:
			salir()

			
	
#se llama a la funcion menu.

menu()







