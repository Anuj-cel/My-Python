              
                                                             # This is PYTHON Tic Tac Game
def start():
    pass
def restart():      
    def getval(index):
        if(xstate[index]==1):
            return 'X'
        elif(ystate[index]==1):
            return 'O'
        else:
            return index
    def checkwin():
        xwin=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for win in xwin:
            if(xstate[win[0]]+xstate[win[1]]+xstate[win[2]]==3):
                print("Game over , X wins ")
                return -1
            elif(ystate[win[0]]+ystate[win[1]]+ystate[win[2]]==3):
                print("Game over , Y wins ")
                return -1
        return 1

    def printbox():
        print("\n")
        print(f" {getval(0)} | {getval(1)} | {getval(2)} ")
        print(f"---|---|---")
        print(f" {getval(3)} | {getval(4)} | {getval(5)} ")
        print(f"---|---|---")
        print(f" {getval(6)} | {getval(7)} | {getval(8)} ")
        print("\n")
        
    if __name__=="__main__":
        print("\nWelcome to PYTHON Tic Tac Game \n")
        xstate=[0,0,0,0,0,0,0,0,0]
        ystate=[0,0,0,0,0,0,0,0,0]
        print(" 0 | 1 | 2 ")
        print("---|---|---")
        print(" 3 | 4 | 5 ")
        print("---|---|---")
        print(" 6 | 7 | 8 ")
        print("\n")
        turn =1
        cnt=0
        while(True):
            if(cnt==8):
                print("Game draw ")
                break
            if(turn ==1):
                print("X's chance")
                flag=1
                while(flag):
                    index=int(input("Enter index : "))
                    if(ystate[index]==0 and xstate[index]==0):
                        xstate[index]=1
                        flag=0
                    else:
                        print("This index has already been filled , enter other index")

                turn =0
            else:
                print("Y's chance")
                flag=1
                while(flag):
                    index=int(input("Enter index : "))
                    if(ystate[index]==0 and xstate[index]==0):
                        ystate[index]=1
                        flag=0
                    else:
                        print("This index has already been filled , enter other index")
                turn =1
            printbox()
            result=checkwin()
            if(result==-1):
                break
            cnt=cnt+1
start=restart 
start()
choice =input("\nDo you want to reatart the game , (yes/no) : ")
while(choice=="yes"): 
    restart()

