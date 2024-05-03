#utf-8 para que pueda leer todos los caracteres 
#una vez que se lee un archivo no se puede volver a leer 
#leer archivo completo
archivo = open("archivos\\lorem_insup.txt", encoding="UTF-8")
#print(archivo.read())

# leer linea por linea 
#\n = salto de linea 
#lineas = archivo.readlines()
#print(lineas)

#leer una sola linea \ se le puede pasar la cantidad de caracteres 
linea_1 = archivo.readline()
print(linea_1)

#cerrar archivó
#no se puede leer una vez cerrado 
# open ,para abrirlo de nuevo
archivo.close()


