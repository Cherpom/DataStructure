print(" *** Summation of each digit ***")
input1 = input("Enter a positive number : ")
num = int(input1);
total = 0
for i in range(len(input1)):
    total += num % 10
    num = num // 10
print("Summation of each digit =  " + str(total))