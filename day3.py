print("welcom to roger youtube channel")
chiose1=input('where do you want to go,type"right","left"do you choose:').lower()

if chiose1 == "left":
    chiose2=input("you arrive at crossroad,which of type do you chiose'swim','wait'").lower()
    if chiose2 == "wait":
        choise3=input("you are so lucky,which of three room do you want to chiose, one yellow,one blue,one red").lower()
        if choise3 =="red":
            print("you are win")
        elif choise3 =="yellow":
            print("you meet richo,game over")
        elif choise3 =="blue":
            print("you are game over")
    else:
        print("you are game over")

else:
    print("game over")