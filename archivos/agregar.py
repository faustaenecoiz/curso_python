with open("archivos\\lorem_insup.txt",'a',  encoding="UTF-8")  as archivo : 
    for i in range (7):
       nombre = input("ingrese su nombre : ")
       archivo.write(f'hola  {nombre}  te quedan {i+1} vidas \n')
 