

user_points = 0
system_points = 0
tie_points = 0

n =10
i =1
   
while i <=n:
    ui = input("enter the input from folling option:snake,gun,water:")
    if ui == "snake" or ui == "gun" or ui == "water":
        list = ["snake","gun","water"]
        import random
        sysi =(random.choice(list))
        print(sysi)
        if ui == sysi:
            print("match tie")
            system_points += 1
            user_points += 1
            tie_points += 1
            print('User Point:',user_points)
            print('System Point:',system_points)
            print('Tie Points :', tie_points)
        elif ui == "snake" and sysi == "gun":
             print("system won")
             system_points += 1
             print('User Point:',user_points)
             print('System Point:',system_points)
        elif ui == "snake" and sysi == "water":
             print("user won")
             user_points += 1
             print('User Point:',user_points)
             print('System Point:',system_points)
        elif ui == "gun" and sysi == "snake":
            print("user won")
            user_points += 1
            print('User Point:',user_points)
            print('System Point:',system_points)
        elif ui == "gun" and sysi == "water":
            print("system won")
            system_points += 1
            print('User Point:',user_points)
            print('System Point:',system_points)
        elif ui == "water" and sysi == "snake":
            print("system won")
            system_points += 1
            print('User Point:',user_points)
            print('System Point:',system_points)
        elif ui == "water" and sysi == "gun":
            print("user won")
            user_points += 1
            print('User Point:',user_points)
            print('System Point:',system_points)
        i =i+1
    else:
        print("invalid input")
        


if (user_points>system_points):
     print("user won, total point",user_points," tie points" ,tie_points)
else:
    print("system won,total points",system_points, " tie points" ,tie_points)






    























    
