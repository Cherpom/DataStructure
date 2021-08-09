def display(num,size,print_count = 0):
    if num < 0 or num == None:
        print("Only Positive & Zero Number ! ! !")
        return
    else:
        if(print_count <= num):
            print("{0:b}".format(print_count).zfill(size))
            return display(num,size,print_count + 1)
        return

input1 = int(input("Enter Number : "))
into_display = pow(2, input1) - 1
display(into_display,input1)