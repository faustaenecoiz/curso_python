#definir variables , y valores
# Consigna : hallar la diferencia porcentual de duracion de horas entre el curso actual , el mas lento , el mas rapido y el promedio
time_min = 2.5 
time_max = 7
general_average = 4 
current_course = 1.5 

percentage_min = 100 - (current_course/ time_min *100)
percentage_max = 100 - (current_course/ time_max *100)
percentage_general_average = 100 - (current_course / general_average *100)
#consigna = ver cuanto material basura se elimna en el curso actual en compracion con los promedios 
trash_average = 5
trash_current = 3.5

percentage_trash = 100 - (general_average/trash_average * 100)
percentage_current = 100 - (current_course / trash_current *100)

#print ( f'el material basura que se elimina de este curso es  {percentage_current}%  ')

print (f'ver 10 horas de este curso equivale a {general_average/current_course *10} horas de un curso promedio ')