
ui = input("enter the input from folling option:snake,gun,water:")
if ui == "snake" or ui == "gun" or ui == "water":
    list = ["snake","gun","water"]
    user_points = 0
    system_points = 0

    n =10
    i =0


        
    while i <=10:
        import random
    

        sysi =(random.choice(list))
        print(sysi)
        if ui == sysi :
           print("match tie")
           system_points = system_points+1
           user_points = user_points +1
        elif ui == "snake" and sysi == "gun":
            print("user won")
            user_points = user_points +1
    
        elif sysi == "water" and ui == "snake":
            print("system won")
            system_points = system_points +1

        elif ui == "gun" and sysin == "snake":
            print("user won")
            user_points = user_points +1

        elif sysin == "gun" and ui == "water":
            print("system won")
            System_points = system_points +1
    
        break

    if (user_points>system_points):
        print("user won, total point:"+user_point)
    else:
        print("system won,total points:"+system_points)

else:
    print("invalid input")




    























    
