input1 = input("Enter Your List : ").split(" ")
display_list = []
num_list = [ int(x) for x in input1 ]
if len(input1) > 2:
    for i in range(len(num_list)):
        for j in range(i + 1,len(num_list)):
            for k in range(j + 1,len(num_list)):
                sum_jk = 0 - (num_list[j] + num_list[k])
                int_i = num_list[i]
                if int_i == sum_jk:
                    another_list = [num_list[i],num_list[j],num_list[k]]
                    if another_list not in display_list:
                        display_list.append(another_list)
    print (display_list)
elif len(input1) <= 2:
    print("Array Input Length Must More Than 2")