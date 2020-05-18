import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
lengthinput=int(input("Enter the length of password you want : "))
for i in range(lengthinput):
    p="".join(random.choices(s))
    print(p,end="")
