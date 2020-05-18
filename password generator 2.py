# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
lengthinput=int(input("Enter the length of password you want : "))
p="".join(random.sample(s,lengthinput))
print(p)



s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
lengthinput=int(input("Enter the length of password you want : "))
p="".join(random.choice(s) for _ in range(lengthinput))
print(p)


# with duplicate characters
import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
lengthinput=int(input("Enter the length of password you want : "))
for i in range(lengthinput):
    p="".join(random.choices(s))
    print(p,end="")
