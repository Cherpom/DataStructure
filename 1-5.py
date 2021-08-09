import timeit

input1 = input("Enter Input : ")

start = timeit.timeit()
num_of_grid = (int(input1) + 2) * 2
half_grid = int(input1) + 2
# (input + 2) * 2 grid

#first line
for i in range(half_grid - 1):
    print(".",end='')
for i in range(1):
    print("#",end='')
for j in range(half_grid):
    print("+",end='')

print("\n",end='')

#Dot in yinyang line
for i in range(int(input1)):
    #Dot
    for j in range(half_grid - i - 2):
        print(".",end='')
    # #
    for j in range(i + 2):
        print("#",end='')
    #plus1
    print("+",end='')
    #hallow in yinyang
    for j in range(int(input1)):
        print("#",end='')
    #plus2
    print("+",end='')
    print("\n",end='')

#2 line # and +
for i in range(2):
    for j in range(half_grid):
        print("#",end='')
    for j in range(half_grid):
        print("+",end='')
    print("\n",end='')

#dot in yinyang line 2
for i in range(int(input1)):
    # #1
    print("#",end='')
    #plus in hallow
    for j in range(int(input1)):
        print("+",end='')
    # #2
    print("#",end='')
    #plus
    for j in range(half_grid - i - 1):
        print("+",end='')
    #Dot
    for j in range(i + 1):
        print(".",end='')
    print("\n",end='')

#last line
for i in range(half_grid):
    print("#",end='')
print("+",end='')
for j in range(half_grid - 1):
    print(".",end='')

print(start)