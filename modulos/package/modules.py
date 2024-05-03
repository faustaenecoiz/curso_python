#un modulo es cualquier archivo .py
#nativos - de terceros - propio . 
#se comporta como un objeto , la funcion creada pasa a ser una propiedad 
#namespace 
#as  asignarle un nuevo nombre 

#se  puede importar el modulo completo , o solo una cosa 
#import modules_hello as lampara 

# se pueden renombrar funciones con as
# acceder al archivo suponiendo que se encuentre en una carpeta aparte 
# importar una carpeta dentro de la carpeta principal 
# from carpeta_nueva.modules_hello import saludar 

#import sys  #= modulo build in 
#ver los modulos que vienen con python 
#print(sys.builtin_module_names)

#agregar el archivo a la ruta especificda 
#sys.path.append = agregar por ruta 

from modulos.package.modules_hello import saludar 



print(saludar(input("ingrese su nombre : ")))