#funciones integradas a python 
numbers = [11, 224, 9 , 111 , 4 ]
#print (max(numbers)) = devuelve el numero mas alto 
#print(min(numbers)) = devuelve el numero mas bajo 


number =  round(190.994848 , 3) #= redondea el numero flotante dejando los decimales que le indiquemos despues de la coma 
#datos vacios = false , none , 0 . 
#print (bool(numbers)) = los datos no vacios los devuelve como true 
#print (all(numbers))  = para que sea true los datos deben ser verdaderos 
#print (sum(numbers)) = suma todos los valores 

notes =[10 , 4 , 3 , 6 , 7 , 9 ]
if sum(notes)/len(notes) >= 7 : 
    print("estas aprobado")
else : 
    print("estas desaprobado")