print("*** Converting hh.mm.ss to seconds ***")
text = input("Enter hh mm ss : ")
data = text.split(" ")
h = int(data[0])
m = int(data[1])
s = int(data[2])
if h<0:
    print("hh(" + str(h) + ") is invalid!")
elif m<0:
    print("mm(" + str(m) + ") is invalid!")
elif s < 0:
    print("ss(" + str(s) + ") is invalid!")
elif m >= 60:
    print("mm(" + str(m) + ") is invalid!")
elif s >= 60:
    print("ss(" + str(s) + ") is invalid!")
else :
    total = h*3600 + m*60 + s
    print("{0:0=2d}".format(h) + ":" + "{0:0=2d}".format(m) + ":" + "{0:0=2d}".format(s) + " = " + f'{total:,}' + " seconds")