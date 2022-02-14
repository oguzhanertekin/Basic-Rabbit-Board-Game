### MAP STRING TO LIST
map_obejcts="*XWCAMP"
str_input= str(input("Please enter feeding map as a list:\n"))
str_input= str_input[1:len(str_input)-1]
list=[]
board_l=[]    #BOARD LIST
for character in str_input:
    if character in map_obejcts:
        list.append(character)
    if character=="]":
        board_l.append(list)
        list=[]
### INPUT DIRECTION AS LIST
command=input("Please enter direction of movements as a list:\n")
command_strip= command.strip("[]")
command_split= command_strip.split(",")
command_list= []
for i in command_split:
    command_list.append(i.strip(" ' "))

### CREATING BOARD FROM LIST
def board(board_l):
    for i in board_l:
        for c in i:
            print(c,end=" ")
        print()

### FIND THE INSTANT LOCATION
for list in board_l:
    for direction in list:
        if direction=="*":
            pos=[board_l.index(list),list.index(direction)] # RABBIT'S POSITION

print("Your board is:")
board(board_l)

score1=0
score_list=["C","A","M"]

def score(x):
    global score1
    if x=="A":
        score1+=5
    elif x=="C":
        score1+=10
    elif x=="M":
        score1-=5

#MOVING COMMAND
for cmd in command_list:
    if cmd=="U":
        if board_l[pos[0]-1][pos[1]]=="W":
            continue
        elif board_l[pos[0]-1][pos[1]]=="P":
            board_l[pos[0]][pos[1]] = "X"
            pos[0] -= 1
            board_l[pos[0]][pos[1]] = "*"
            break

        elif pos[0]==0:
            continue
        
        elif board_l[pos[0]-1][pos[1]] in score_list:
            score((board_l[pos[0]-1][pos[1]]))
            board_l[pos[0]][pos[1]] = "X"
            pos[0] -= 1
            board_l[pos[0]][pos[1]] = "*"
        else:
            board_l[pos[0]][pos[1]]="X"
            pos[0]-=1
            board_l[pos[0]][pos[1]]="*"

    elif cmd=="D":
        if pos[0]==len(board_l)-1:
            continue
        elif board_l[pos[0]+1][pos[1]]=="W":
            continue
        elif board_l[pos[0] + 1][pos[1]] in score_list:
            score((board_l[pos[0] + 1][pos[1]]))
            board_l[pos[0]][pos[1]] = "X"
            pos[0] += 1
            board_l[pos[0]][pos[1]] = "*"

        elif board_l[pos[0] + 1][pos[1]]=="P":
            board_l[pos[0]][pos[1]] = "X"
            pos[0] += 1
            board_l[pos[0]][pos[1]] = "*"
            break

        else:
            board_l[pos[0]][pos[1]]= "X"
            pos[0]+= 1
            board_l[pos[0]][pos[1]]="*"

    elif cmd == "R":
        if pos[1] == len(board_l[0])-1:
            continue
        elif board_l[pos[0]][pos[1]+1] == "W":
            continue
        elif board_l[pos[0]][pos[1]+1] in score_list:
            score((board_l[pos[0]][pos[1]+1]))
            board_l[pos[0]][pos[1]] = "X"
            pos[1] += 1
            board_l[pos[0]][pos[1]] = "*"

        elif board_l[pos[0]][pos[1]+1]=="P":
            board_l[pos[0]][pos[1]] = "X"
            pos[1] += 1
            board_l[pos[0]][pos[1]] = "*"
            break
        else:
            board_l[pos[0]][pos[1]] = "X"
            pos[1] += 1
            board_l[pos[0]][pos[1]] = "*"

    elif cmd == "L":
        if pos[1] ==0:
            continue
        elif board_l[pos[0]][pos[1] - 1] == "W":
            continue
        elif board_l[pos[0]][pos[1] - 1] in score_list:
            score((board_l[pos[0]][pos[1] - 1]))
            board_l[pos[0]][pos[1]] = "X"
            pos[1] -= 1
            board_l[pos[0]][pos[1]] = "*"

        elif board_l[pos[0]][pos[1] - 1]=="P":
            board_l[pos[0]][pos[1]] = "X"
            pos[1] -= 1
            board_l[pos[0]][pos[1]] = "*"
            break
        else:
            board_l[pos[0]][pos[1]] = "X"
            pos[1] -= 1
            board_l[pos[0]][pos[1]] = "*"

print("Your output should be like this:")
board(board_l)
print("Your score is: ",score1)