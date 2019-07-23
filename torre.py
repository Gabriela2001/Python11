import os
import time

'''------------------------------------------------------------------------------------------------------------------------'''

Productos = [
	[1,"Galleta Gama   ", 005.00],  
	[2,"Clorox         ", 15.00], 
	[3,"Jamon          ", 15.00], 
	[4,"Pasta          ", 15.00], 
	[5,"Desodorante    ", 40.00], 
	[6,"Jabon de cuerpo", 5.00], 
	[7,"Papel higienico", 20.00], 
	[8,"sal            ", 1.00], 
	[9,"azucar         ", 6.00], 
	[10,"Caja de leche ", 11.00], 
	[11,"Detergente    ", 50.00], 
	[12,"Cafe          ", 10.50], 
	[13,"Bolsa de crema", 05.00], 
	[14,"Corn Flakes   ", 025.00], 
	[15,"Blusa         ", 040.00], 
	[16,"Pantalon      ", 120.00], 
	[17,"Sueter        ", 100.00], 
	[18,"Zapatos       ", 250.00], 
	[19,"Pantaloneta   ", 100.00], 
	[20,"Gorra         ", 050.00]]


'''----------------------------------------------------------------------------------------------------------------------'''


def Compra():

	print
	print"------------------------------------"
	print" COD.|    PRODUCTO   |    PRECIO   "
	print"------------------------------------"
	
	for x in Productos:
		print "  "+ str(x[0]) + "  | "+ str(x[1]) + "  |   "+ str(x[2])

	print
	produc = input("INGRESE CODIG0: ")
	print
	numero = input("INGRESE NUMERO DE UNIDADES: ")
	print
	print"TOTAL A PAGAR"
	total= Productos[produc-1][2]*numero
	print  total           
	print
	print
	print"-----------------DATOS PARA LA FACTURA------------------------"
	print
	nombre = raw_input("INTRODUZCA UN NOMBRE Y APELLIDO: ")
	print
	nit = input("INGRESE NUMERO DE NIT: ")
	print"--------------------------------------------------------------"



	def factura():
		os.system('cls')

		print
		print"                                   LA TORRE"
		print"                   2da. ave. 3ra. calle zona5 col. Margaritas"
		print"                             Villa Nueva, Guatemala"
		print"                                 Tel: 4455-6655"
		print
		print
		print
		print" NOMBRE: " + str(nombre) + "          FECHA: " +str((time.strftime("%d/%m/%y")))+ "          NIT: " + str(nit)
		print
		print
		print
		print"|----------------------------------------------------------------------------|"
		print"|                              DESCRIPCION                                   |"
		print"|----------------------------------------------------------------------------|"
		print"| COD.  |        PRODUCTO      |     PRECIO UNITARIO     |   TOTAL A PAGAR   |"
		print"|-------|----------------------|-------------------------|-------------------|"
		print"|  " + str(Productos[produc-1][0]) + "   |     "+str(Productos[produc-1][1])+ "   |           "+str(Productos[produc-1][2]) + "          |       " + str(total) 
		print"|-------|----------------------|-------------------------|-------------------|"
		print"|       |                      |                         |                   |"
		print"|-------|----------------------|-------------------------|-------------------|"
		print"|       |                      |                         |                   |"
		print"|-------|----------------------|-------------------------|-------------------|"
		print"|       |                      |                         |                   |"
		print"|-------|----------------------|-------------------------|-------------------|"
		print"|       |                      |                         |                   |"
		print"|-------|----------------------|-------------------------|-------------------|"
		print"|       |                      |                         |                   |"
		print"|-------|----------------------|-------------------------|-------------------|"
		print"|       |                      |                         |                   |"
		print"|-------|----------------------|-------------------------|-------------------|"
		print 
		print
		print
		print
		print"                       TOTAL A PAGAR: " + str(total)
		print"                                     ------------"

	factura()
'''------------------------------------------------------------------------------------------------------------------------'''
print
print
dato = raw_input("DESEA COMPRAR ALGUN PRODUCTO? ")			
if dato == "si" or "SI":
	Compra()
else:
	print
	print"GRACIAS POR UTILIZAR NUESTROS PRODUCTOS."

'''------------------------------------------------------------------------------------------------------------------------'''