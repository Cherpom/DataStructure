def findMax(list1,max_num=-10000):
    if len(list1) == 0:
        return max_num
    else:
        number = list1.pop()
        if number > max_num:
            max_num = number
        return findMax(list1,max_num)

def sort(lst,out,length):
    if len(out) < length:
        max_from_findmax = findMax(lst.copy())
        out.append(max_from_findmax)
        lst.remove(max_from_findmax)
        sort(lst, out, length)
        if len(out) == length:
            return out
    else:
        return out

input1 = [int(i) for i in input("Enter your List : ").split(',')]
lst = list()
display = sort(input1,lst,len(input1))
print(f'List after Sorted : {display}')