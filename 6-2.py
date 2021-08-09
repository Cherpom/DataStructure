def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e >= l[0]]) +\
            [l[0]] +\
            quick_sort([e for e in l[1:] if e < l[0]])

input1 = input("Enter your List : ").split(',')
display = [int(i) for i in quick_sort(input1)]
print(f'List after Sorted : {display}')