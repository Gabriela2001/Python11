print  "----------------------------------------------------------------------------"
print  "-----------------CLASIFICACION DE JUBILACIONES DEL IGSS---------------------"
print  "----------------------------------------------------------------------------"
print 
print 

edad = input ("Ingrese su edad: ")
antiguedad = input ("Ingrese la cantidad de anios que trabajo: ")

if edad >= 60 and antiguedad < 25 :
	print "_________________________"
	print "---Jubilacion por edad---"
	print "_________________________"

elif edad < 60 and antiguedad >= 25 :
	print "______________________________________"
	print "---Jubilacion por antiguedad joven---"
	print "______________________________________"

elif edad >= 60 and antiguedad >= 25 :
	print "______________________________________"
	print "---Jubilacion por antiguedad adulta---"
	print "______________________________________"

