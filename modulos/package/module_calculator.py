#OPERACIONES MATEMATICAS 

def suma (a,b):
    return a + b
def multiplicacion (a,b):
    return a*b 
def resta (a,b):
    return a - b
def division(a,b):
    if a ==0  or b == 0 :
        print(" ERROR! no se puede dividir por zero") 
    else:
        return a/b
def potencia (a, b ): 
     return a**b

n1 = int(input("ingrese un numero "))
n2 = int(input("ingrese otro numero "))

print(f'La Suma  es : {suma(n1, n2 )}')
print(f'La Multiplicacion es: {multiplicacion(n1, n2 )}')
print(f'La Resta  es :  {resta(n1, n2 )}')
print(f'La Division es : {division(n1, n2 )}')
print(f'La potencia  es : {potencia(n1, n2 )}')


#SELECCIONAR OPERACION 
    