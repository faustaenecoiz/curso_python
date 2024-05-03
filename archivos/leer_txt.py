with open("archivos\\lorem_insup.txt", encoding="UTF-8")  as archivo : 
    contenido = archivo.read()
    print(contenido)
#no hace falta cerrarlo con with open 