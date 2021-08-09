def print1ToN(n):
    if n < 2:
        print(f'1',end=" ")
        return None
    else:
        print1ToN(n-1)
        print(f'{n}',end=' ')

def printNto1(n):
    if n < 2:
        print(f'1',end=" ")
        return None
    else:
        print(f'{n}',end=' ')
        printNto1(n-1)


n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)