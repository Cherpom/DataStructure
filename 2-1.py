input1 = input("Enter String : ")
list1 = map(list,input1)
forlist = list(list1)
count = 0
dict1 = {}
final = []
for i in range(len(forlist)):
    if(forlist[i][0] not in dict1):
        dict1[forlist[i][0]] = count
        count += 1
    final.append(dict1[forlist[i][0]])
print(final)