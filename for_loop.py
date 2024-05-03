#recorriedno listas , tuplas y conjuntos 
notes = [10 , 9 , 4 , 2 ]
for note in notes: 
    print ( note)
names = ["fausta", "benja" , "raul" , "lucas"]
#recorrer dos listas al mismom tiempo , deben tener los mismos elemntos 
for name , note in zip(names , notes):
    print(f'recorriendo names: {name}')
    print(f'recorriendo notes: {note}')

#recorrer una lista por su indice   
for note in enumerate(notes):
    print(note)
#for else
for note in notes :
    print(note)
#el else se muestra cuando finaliza el bucle 
else: 
    print ("el bucle ha finalizado ")
    
    
#iterar diccionario
#items devuelve una tupla con una clave y valor 
diccionario =dict (nombre = "faustina" , edad = 18 , apellido ="enecoiz")
for key in diccionario.items()  :
    llave = key[0]
    valor = key [1]
    print (f'la llave es {llave} y el valor es {valor}')

#salteando un valor 
for name in names : 
    if name == "raul" :
        continue
    print(f'hola soy {name}')
#evitar que el bucle se ejecute , se pone break , cuando encuentra un break no ejecuta nada mas despues del else 


#iterar una cadena de caracteres 
cadena = "hola como estas "
for caracter in cadena : 
    print (caracter)
#duplicando valores
notes_duplicadas = [x*2 for x in notes]
print(notes_duplicadas)