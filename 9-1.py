def bubble_sort(data):
    step = 1
    for last in range(len(data) - 1, -1, -1):
        swap = False
        tmp = None
        for i in range(last):
            if data[i] > data[i + 1]:
                tmp = data[i]
                data[i], data[i + 1] = data[i + 1], data[i]
                swap = True
        if not swap:
            return data
def bubblesort(list):
# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    print(list)
        

if __name__ == '__main__':
    inp = [int(a) for a in input('Enter Input : ').split()]
    bubblesort(inp)