#como las funciones anonimas de js , retornan automaticamente 
multiplicacion =  lambda x : x*7
print (multiplicacion (int((input("ingrese un numero ")))))


#creando una funcion para saber si el numero es par o impar
numeros = [12 , 3 , 2 , 4 ,88, 9 , 33 , 17 ]
#va a recorrer la lista y si los valores son true , lo va a agregar a una lista 
#def par(numero) :
 #   if (numero%2==0):
  #      return True
  
#def impar (numero) : 
 #   if (numero%2==1):
  #   return True
#la funcion filter lo que hace es ejecutar cada uno de los valores de un iterable 
#print(f'los numeros pares son {list(filter(par, numeros))}' )
#print(f'los numeros impares son {list(filter(impar , numeros))}' )


numero_pares = filter(lambda numero : numero%2==0 , numeros)
numero_impares = filter(lambda numero : numero%2==1 , numeros)
print(f'los numeros pares son : {list(numero_pares)}')
print(f'los numeros impares son : {list(numero_impares)}')
