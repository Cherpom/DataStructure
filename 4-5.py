input1 = input("Enter Input (Normal, Mirror) : ").split(" ")
input1 = [list(i) for i in input1]
item_stack = list()
mirror_stack = []
mirror_explosion = 0

#Mirror
for i in range(len(input1[1])):
    mirror_stack.append(input1[1][i])
    if (len(mirror_stack) < 3):
        pass
    else:
        if(mirror_stack[len(mirror_stack)-1] == mirror_stack[len(mirror_stack)-2] == mirror_stack[len(mirror_stack)-3]):
            mirror_explosion = mirror_explosion + 1
            item_stack.append(mirror_stack.pop())
            [mirror_stack.pop() for i in range(2)]
        else:
            pass
display_item_stack = item_stack.copy()
item_stack.reverse()

#Normal
fail_attemp = 0
normal_stack = list()
normal_explosion = 0
for i in range(len(input1[0])):
    normal_stack.append(input1[0][i])
    if (len(normal_stack) < 3):
        pass
    else:
        if(normal_stack[len(normal_stack)-1] == normal_stack[len(normal_stack)-2] == normal_stack[len(normal_stack)-3]):
            if(len(item_stack) != 0):
                normal_stack.insert(-1,item_stack.pop(0))
                if(normal_stack[len(normal_stack)-1] == normal_stack[len(normal_stack)-2] == normal_stack[len(normal_stack)-3]):
                    fail_attemp = fail_attemp + 1
            if(normal_stack[len(normal_stack)-1] == normal_stack[len(normal_stack)-2] == normal_stack[len(normal_stack)-3]):
                normal_explosion = normal_explosion + 1
                [normal_stack.pop() for i in range(3)]
        else:
            pass
normal_stack.reverse()

#print format
print("NORMAL :")
print(len(normal_stack))
if(len(normal_stack) == 0):
    print("Empty")
else:
    for i in range(len(normal_stack)):
        print(normal_stack[i],end='')
    print()
print(normal_explosion-fail_attemp, "Explosive(s) ! ! ! (NORMAL)")
if(fail_attemp != 0):
    print("Failed Interrupted", fail_attemp, "Bomb(s)")

print("------------MIRROR------------")
print(": RORRIM")
print(len(mirror_stack))
if(len(mirror_stack) == 0):
    print("ytpmE")
else:
    for i in range(len(mirror_stack)):
        print(mirror_stack[i],end='')
    print()
print("(RORRIM) ! ! ! (s)evisolpxE", mirror_explosion)