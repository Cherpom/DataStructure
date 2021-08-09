def bitterPlus(lst,out=0):
    if len(lst) == 0:
        return out
    elif len(lst)>0:
        out = out + lst.pop()
        return bitterPlus(lst,out)
def sourProduct(lst,out=1):
    if len(lst) == 0:
        return out
    elif len(lst)>0:
        out = out * lst.pop()
        return sourProduct(lst,out)

def sourList(lst,out,length):
    if length == 0:
        return out
    elif length >= len(lst) and len(lst) != 0:
        temp = lst.pop(0)
        out.append(int(temp[0]))
        sourList(lst,out,length)
    return out

def bitterList(lst,out,length):
    if length == 0:
        return out
    elif length >= len(lst) and len(lst) != 0:
        temp = lst.pop(0)
        out.append(int(temp[1]))
        bitterList(lst,out,length)
        return out

input1 = input("Enter Input : ").split(",")
in_list = list(map(lambda x:x.split(), input1))
sourlist = sourList(in_list.copy(),list(),len(in_list))
bitterlist = bitterList(in_list.copy(),list(),len(in_list))
print(in_list)
print(bitterlist)
print(sourlist)
#print(sourProduct(sourlist))
#print(bitterPlus(bitterlist))
#print(abs(bitterPlus(bitterlist) - sourProduct(sourlist)))
