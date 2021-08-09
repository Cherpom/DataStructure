def newrange(start, end = None, step = None):
    if end is None:
        end = start + 0.00
        start = 0.00
    if step is None:
        step = 1.00
    print("(",end="")
    while True:
        if step > 0 and start >= end:
            break
        elif step < 0 and start <= end:
            break

        print (round(start, 3), end = "")

        if start + step < end:
            print(", ", end = "")
        else:
            print("",end = "")
        start = start + step
    print(")")

print("*** New Range ***")
input1 = input("Enter Input : ").split(" ")

if len(input1) == 1:
    newrange(float(input1[0]))
elif len(input1) == 2:
    newrange(float(input1[0]), float(input1[1]))
elif len(input1) == 3:
    newrange(float(input1[0]), float(input1[1]), float(input1[2]))