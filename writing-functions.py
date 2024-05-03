def saludar (nombre):
    print(f'hola {nombre}')
saludar(input("ingrese un nombre : "))

def create_password (num):
    chars = "abcdefghijkmnñlopqrstuv"
    #pasar el numero a string para obtener el primer numero 
    numero_enetero = str(num)
    num = int(numero_enetero[0])
    #al numero pasado le resta 4
    char1 = num - 4
    char2 = num
    #al numero pasado le resta 8 
    char3 = num - 8 
    #elegir un caracter de las letras , y usar el indece de char1 ,char2 , char3 
    #y despues multiplico al numero que le pase por 4 
    password = f'{chars[char1]}{chars[char2]}{chars[char3]}{num*4}'
    #reotornar valores para guardarlos y despues utilizarlo 
    #se pueden retornar multiples valores
    return password , num
print(create_password(int(input("ingrese un numero : "))) )




