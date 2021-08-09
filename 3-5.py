input1 = input("Enter Input : ").split(",")
input1 = [i.split(" ") for i in input1]
stack = []
rerange_stack = []
max_index_height = 0

def rerange():
    if(len(stack) == 0):
        return 0
    rerange_stack = []
    #print("From rerange function, stack = ",end='')
    #print(stack)
    max_index_height = stack.index(max(stack))
    #print("From rerange function, max_index_height = " + str(max_index_height))
    rerange_stack.append(stack[max_index_height])
    for i in range(max_index_height,len(stack)):
        for j in range(i+1,len(stack)):
            if(stack[j]<stack[i]):
                rerange_stack.append(stack[j])
            break
    #print("From rerange function, rerange_stack = ",end='')
    #print(rerange_stack)
    return len(rerange_stack)

for i in range(len(input1)):
    if(input1[i][0] == 'A'):
        stack.append(int(input1[i][1]))
    elif(input1[i][0] == 'B'):
        print(rerange())
    elif(input1[i][0] == 'S'):
        #print(stack)
        for j in range(len(stack)):
            if(stack[j]%2==1):
                stack[j] += 2
            else:
                stack[j] -= 1