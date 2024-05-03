#listas/logica del array,datos que se pueden ir modificando 
 
colores =  ["azul", "rojo", "amarillo"]


#tuplas cuando solo puedo leer datos que no se van a modificar
 
numeros = (1, 2 , 3 , 4 , 5 , 6 )
#se puede crear una tupla de un solo valor 
name = "john" , 


#crear un conjunto ,elementos desordenados que pueden cambiar de posicion ,
# se puede redifinir la variable pero no se pueden cambiar los valores de los elementos 

#no pueden haber datos duplicados 
numeritos = { 11 , 12 , 13 , 14 }

#tmb se puede crear un conjunto con set
conjunto = set(["dato1" , "dato2"])
# conjuntos anidados 
conjunto1 = frozenset(["faustina" , "enecoiz", 18])
conjunto2 = {conjunto1 , "fausta"}


#teoria de los conjuntos , subconjunto y superconjunto 
resultado = conjunto1.issubset(conjunto2)
#tmb se puede usar issuperset 
#va devolver true cuando los elementos del conjunto 2 sean distinitos a los elementos del conjunto 1 
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)







#crear un diccionario/similar a un objeto
diccionario = {
    'nombre' : "faustina",
    'mayor de edad' : True ,
    'edad': 18  
}

#crear un diccionario con valores vacios 
diccionario2 = dict.fromkeys(["nombre", "apellido" , "edad "])
# a la hora de imprimirlo de lo llama por el nombre de la propiedad 
print(diccionario['mayor de edad'])
