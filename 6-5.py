def staircase(n,underscore = None):
    if n == 0:
        print("Not Draw!")
    if(underscore is None):
        if n > 0:
            underscore = n
        else:
            underscore = -n
    display = str()
    if n==1:
        display = "_"*(underscore-1) +"#"
        print(display)
    elif n > 0:
        staircase(n-1,underscore)
        display = "_"*(underscore-n) + "#"*n
        print(display)
    if n == -1:
        display = "#"*underscore
        print(display)
    elif n < 0:
        staircase(n+1,underscore)
        display = "_"*((-n)-1) + "#"*(underscore-(((-n)-1)))
        print(display)

staircase(int(input("Enter Input : ")))