user_text = input("ingrese un texto : ")
count_words = len (user_text.split(" "))

#si el tiempo de las palabras es mayor  60 segundos , le pedirá  un texto más corto . 
#tambien se puede hacer de otra forma , si la cantidad de palabras es mayor 120 le pedirá un texto más corto 
# 2 palabras = 1 segundo , si tenemos una frase de 10 palabras va a tardae 5 en decirla xq es la mitad 

if (count_words/2) >= 60 :
    print ("estas ecribiendo mucho , ingresa un texto más corto ")
else :
    print(f'tardarias en decir la frase {count_words/2} segundos')
