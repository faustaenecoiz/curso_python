with open("archivos\\lorem_insup.txt",'w',  encoding="UTF-8")  as archivo : 

#archivo.write("sobreescribir el archivo")
#ambas sobreescriben 
 #pasarle una lista con las lineas 
 #se cambia en el txt 
 archivo.writelines(["hola susi\n" , "el mundo espera\n"])