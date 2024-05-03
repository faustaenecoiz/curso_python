# anotar los alumnos resgistrados hoy 
# el mayor sera el profesor y el menor el asistente 

def alumnos_resgistrados (cantidad) :
    alumnos = []
#range = se va a repetir en un rango de tantas veces :
    for i in range (cantidad) :
     nombre = input ("ingrese su nombre :")
     edad = int(input ("ingrese su edad : "))
     alumno = (nombre , edad )
     alumnos.append(alumno)
     #oredena la lista en base al segundo parametro  
    alumnos.sort(key=lambda x:x[1])
    #primer [0] edad , segundo [0] nombre 
    asistente = alumnos [0][0]
    profesor = alumnos [-1][0]
    return asistente , profesor

asistente , profesor = alumnos_resgistrados(int(input("cuantos alumnos asistieron hoy?"))) 
print(f'el profesor es {profesor} y el asistente es {asistente}')
