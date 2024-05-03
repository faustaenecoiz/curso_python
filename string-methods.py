name = "richiardi"

impresion = name.split("i")
print (impresion)
#dir = funcion , cosas que podemos hacer con esa cadena
# len = funcion , cuenta los caracteres de una cadena 


#upper = convierte todo  a mayuscula 
#capitalize = primera letra con mayuscula 
#lower = todo minuscula 
#index = busca algo con la logica de posicion de un array , si no lo encuentra tira una excepcion  
#isnumeric , is alpha = devuelve true si es numerico o alfanumerico 
#count = cuantas veces se encontro tal cosa 
#endswith , starswith = si empieza o termina con tal cosa 
#replace = reemplaza un valor por otro 
#split = separa cadenas y devuelve en forma de lista 



if name.startswith("r"):
    name = name.capitalize()
    print(name)
else :
    name.replace("richard" , input ("ingrese su apellido "))
    print(name)

    