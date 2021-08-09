input1 = input("Enter Input : ").split(" ")
stack = []
combo = 0
for i in range(len(input1)):
    stack.append(input1[i])
    if (len(stack) < 3):
        #print(stack[-1], end=" ")
        pass
    else:
        if(stack[len(stack)-1] == stack[len(stack)-2] == stack[len(stack)-3]):
            #print(stack, end=" ")
            combo = combo + 1
            [stack.pop() for i in range(3)]
        else:
            pass
print(len(stack))
stack.reverse()
if(len(stack) != 0):
    for i in range(len(stack)):
        print(stack[i], end="")
else:
    print("Empty",end="")
print()
if(combo > 1):
    print("Combo : " + str(combo) + " ! ! !")