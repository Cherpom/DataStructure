print("*** multiplication or sum ***")
input1 = input("Enter num1 num2 : ")
list = input1.split(" ")
num1 = int(list[0])
num2 = int(list[1])
sum = str(num1 + num2)
product = str(num1 * num2)
if(num1 * num2 > 1000):
    print ("The result is " + sum)
elif(num1 * num2 <= 1000):
    print ("The result is " + product)