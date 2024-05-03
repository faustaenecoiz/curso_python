#forma no optima 
#def suma (lista):
# numeros_sumados = 0 
# for numero in lista :
#     numeros_sumados = numeros_sumados + numero 
# return numeros_sumados
#resultado = suma([8 , 4 , 5, 9 ])
#print(f'la suma es {resultado}')

#utilizando el parametro args 
#el * hace que todos los parametros sean uno solo , en este caso todo los valores que le pase como parametro va a ser una lista llamada numeros 
#no se puede pasar otro parametros despues de args 
def suma (nombre , *numeros) : 
   return  f'hola {nombre}  , la suma es {sum(numeros)}'
    
resultado = suma("benja" , 1,4,4,3,2,8)
print(resultado)
agradecimiento = input("")
print("de nada facha te quiero mucho ")


 
