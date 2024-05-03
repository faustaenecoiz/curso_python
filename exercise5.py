# funcion que imprima los numeros primos entre 0 y le pasamos 


# esta funcion verifica si el numero es primo , si no lo es retorna false 
def retornar_primos(num) : 
    for i in range(2 , num-1) : 
        if num%i == 0 : return False
    return True
# esta funcion guarda los numeros desde el 2 hasta el numero que le pasamos +1 para verificar cuantos numeros primos hay. 
def mostrar_numeros(num) : 
    primos = []
    for i in range (2 , num+1) : 
        resultado = retornar_primos(i)
        #si es primo se agrega a una lista 
        if resultado == True :
            primos.append (i)
    return primos
print(mostrar_numeros(int(input("ingrese un numerin : "))))
        