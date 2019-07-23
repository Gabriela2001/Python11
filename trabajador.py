print 
print "---------------------------PREMIACION POR DESEMPENO----------------------------"
print
print "El supervisor educativo ha decidido otorgar un bono por desempeno a todos los profesores segun la puntuacion obtenida. "
print 
print
puntos = input("Ingrese su puntuacion: ")

def Calcular():
	print
	print "--------------------------------------------------------------------------------"
	if puntos <= 100:
		print "Felicidades! Has ganado 1 salario en recompensa por tu buen desempeno."
	elif puntos <= 150:
		print "Felicidades! Has ganado 2 salario en recompensa por tu buen desempeno."
	else:
		print "Felicidades! Has ganado 3 salario en recompensa por tu buen desempeno."
		
Calcular()