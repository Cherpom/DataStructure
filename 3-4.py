input1 = input("Enter Input : ").split(",")
input1 = [i.split(" ") for i in input1]
stack = []
for i in range(len(input1)):
    if(input1[i][0] == 'A'):
        if(len(stack) == 0):
            stack.append(int(input1[i][1]))
        else:
            for j in stack[::-1]:
                if(j > int(input1[i][1])):
                    stack.append(int(input1[i][1]))
                    break
                else:
                    stack.pop()
                    if(len(stack) == 0):
                        stack.append(int(input1[i][1]))

    elif(input1[i][0] == 'B'):
        print(len(stack))