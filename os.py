import os
from stat import *

'''
	Funcion para cambiar ubicacion
'''
def cambiar_ubicacion(path_rel):
	print "\n########### NUEVA UBICACION #################"
	if os.access(path_rel,os.X_OK):
		os.chdir(path_rel)
		print "directorio cambiado."
		return True
	else:
		return False

'''
	Funcion para mostrar permisos
'''
def mostrar_permisos(path_rel):
	print "\n############ PERMISOS ("+ path_rel +") ################"
	print "Existe: " + str(os.access(path_rel,os.F_OK))
	print "Lectura: " + str(os.access(path_rel,os.R_OK))
	print "Escritura: " + str(os.access(path_rel,os.W_OK))
	print "Ejecucion: " + str(os.access(path_rel,os.X_OK))


'''
	MAIN
'''

print "\n########### DIRECTORIO ACTUAL #################"
mi_ubi = os.getcwd()
print mi_ubi
print os.path.abspath(".")

print "\n########### DIRECTORIO NUEVO #################"
if not os.access("temp",os.F_OK):
	os.mkdir(mi_ubi+"/temp",0600)
	print "directorio creado"
else:
	print "directorio ya existe"


if not cambiar_ubicacion("temp"):
	print "no tiene los permisos para acceder a este directorio."

	print "\n############ CAMBIAR PERMISOS ################"
	os.chmod("temp",S_IXUSR)
	print "permisos cambiados."

	mostrar_permisos("temp")
	cambiar_ubicacion("temp")
else:
	print os.getcwd()


