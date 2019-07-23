
print "----------------------------------------------------"
print "----------PORCENTAJE DE ALUMNOS Y ALUMNAS-----------"
print "----------------------------------------------------"
print
print

mujeres = input (" Ingrese la cantidad de alumnos que hay en el salon (hombres) : ")
print
hombres = input (" Ingrese la cantidad de alumnas que hay en el salon (mujeres) : ")
alumnos = mujeres + hombres

porcentajemujeres = 100 * mujeres / alumnos
porcentajehombres = 100 * hombres / alumnos
print
print
print "---------------------------------------------------------------"
print " -El porcentaje de mujeres que hay en el salon es de: " + str(porcentajemujeres)
print
print " -El porcentaje de hombres que hay en el salon es de: " + str(porcentajehombres)
print "----------------------------------------------------------------"




