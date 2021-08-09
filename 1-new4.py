def check_surrounding(i,j):
    total = 0
    #Top corner & top frame
    if(i == 0):
        if(j == 0):
            #check [0][1],[1][0],[1][1]
            if(lst_input[0][1] == "#"):
                total += 1
            if(lst_input[1][0] == "#"):
                total += 1
            if(lst_input[1][1] == "#"):
                total += 1
        elif(j == 4):
            #check [0][3],[1][3],[1][4]
            if(lst_input[0][3] == "#"):
                total += 1
            if(lst_input[1][3] == "#"):
                total += 1
            if(lst_input[1][4] == "#"):
                total += 1
        else:
            #check surrounds
            for a in range(2):
                for b in range(3):
                    if(lst_input[i+a][j-1+b] == "#"):
                        total += 1
    #bottom corner & bottom frame
    elif(i == 4):
        if(j == 0):
            #check [3][0],[3][1],[4][1]
            if(lst_input[3][0] == "#"):
                total += 1
            if(lst_input[3][1] == "#"):
                total += 1
            if(lst_input[4][1] == "#"):
                total += 1
        elif(j == 4):
            #check [3][3],[3,4],[4][3]
            if(lst_input[3][3] == "#"):
                total += 1
            if(lst_input[3][4] == "#"):
                total += 1
            if(lst_input[4][3] == "#"):
                total += 1
        else:
            #check surrounds
            for a in range(2):
                for b in range(3):
                    if(lst_input[i+a-1][j-1+b] == "#"):
                        total += 1
    #left frame
    elif(j == 0 and i != 0):
        for a in range(3):
                for b in range(2):
                    if(lst_input[i+a-1][j+b] == "#"):
                        total += 1
    #right frame
    elif(j == 4 and i != 0):
        for a in range(3):
                for b in range(2):
                    if(lst_input[i+a-1][j+b-1] == "#"):
                        total += 1
    else:
        for a in range(3):
                for b in range(3):
                    if(lst_input[i+a-1][j+b-1] == "#"):
                        total += 1
    return str(total)

def num_grid(lst):
    for i in range(5):
        for j in range(5):
            if(lst[i][j] == '-'):
                lst[i][j] = check_surrounding(i,j)
    return lst

'''lst_input = [
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
    ["-","-","#","-","-"],
    ["-","-","-","-","-"],
    ["-","-","-","-","-"]
]'''

print('*** Minesweeper ***')
lst_input = []
input_list = input("Enter input(5x5) : ").split(",")
for e in input_list:
  lst_input.append([i for i in e.split()])
print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")