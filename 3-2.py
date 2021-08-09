input_list = input("Enter Input : ").split(",")
test_list = []
for i in input_list:
    test_list.append(i.split(" "))
for i in range(len(test_list)):
    test_list[i] = [int(j) for j in test_list[i]]
stack = []
for i in range(len(test_list)):
    if(len(stack) == 0):
        stack.append(test_list[i])
    else:
        a = stack.pop()
        if(int(a[0]) >= int(test_list[i][0])):
            stack.append(a)
            stack.append(test_list[i])
        else:
            stack.append(a)
            for j in stack[::-1]:
                if(int(j[0]) < int(test_list[i][0])):
                    b = stack.pop()
                    print(int(b[1]))
                else:
                    #stack.append(test_list[i])
                    break
            stack.append(test_list[i])