"""
qualification = 6
practice_work = 10
for_aprove = 7
if qualification == 6 :
    if (qualification + practice_work)/2 >= for_aprove :
        print ("you passed the year ")
    else :
        print ("reproved")
elif qualification > 7 :
    print ("aproved")
elif qualification < 6 : 
    print (" reproved")


else : 
    print ( " reproved ")
"""
#programa que si aprobó el primer examen y asistio tiene la posibilidad de dar otro
#si no aprobo el primero pero asistio todas las clases puede dra un tp

exam = 10
assistence = False
exam_2 = 2
if exam >= 7  & assistence == True: 
    print (" dont worry , you have a second chance to try ")
    exam_2 = 4
    if exam_2 >= 7: 
        print ("cograts")
        print (exam_2)
        if exam_2 > 9 :
            print ("you're the best , why you didnt study in the first time mother fucker bitch???")
    else :
        print ("you have to try again next year")
        print(exam_2)
elif assistence == True :
    print("you have a chance to give me a practice work ")
    practice_work = 9 
    if practice_work >= 7 :
        print ("congrats")
    else :
        print ( " no congrats ")
    

        
else : 
    print("you cant try again because you didnt aprove the first exam or you dont assits a class")

    
