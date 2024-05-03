#hacer un programa que determine cual es el nimero mas grande entre tres y muestre en pantalla 
number1 = int (input("ingrese un numero :"))
number2 = int (input("ingrese un numero :"))
number3 = int (input("ingrese un numero :"))

if number1 > number2 and number1 > number3 :
    print (f'el numero mas grande es {number1}')
elif number2 > number1 and number2 > number3: 
    print (f'el numero mas grande es {number2}')
elif number3 > number1 and number3 > number2 : 
    print (f'el numero mas grande es {number3}')

    
    