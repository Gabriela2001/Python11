#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "MENU Registros/n/n1)-Nuevo/n2)-Mostrar/n3" - "Eliminar Registros"

opcion = raw_input("Elige una opcion")

if opcion =="1":
	print "Nuevo Registro/n"
	archivo = open("progra.csv","a")

	pais = raw_input (u"Ingrese el nombre del país: ")
	capital = raw_input (u"Ingrese la capital del país: ")

	print "Se han guardado: " + país "," + capital 

	archivo.write(nombre)
	archivo.write(",")
	archivo.write(telefono",/n")
	archivo.write(nombre","telefono",/n")

	archivo.close()

elif opcion == "2":
	print "Mostrar Registros/n"
	archivo = open("progra.csv")

	print (archivo.read())

	archivo.close()

elif opcion == "3":
	archivo = open("progra.csv","a")
	archivo.truncate()

	print "Registros elmininados"

	archibo.close()

else: 
	print "Debes de elegir una opcion anterior"
