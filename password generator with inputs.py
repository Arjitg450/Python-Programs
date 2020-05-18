import random
import pyperclip
def inpp():

    
    exit_input=int(input("If you want to exit PRESS 2 and then PRESS Enter\nFor a new password PRESS 3 and then PRESS Enter\nTo test the password PRESS 4 and then PRESS Enter\n" ))
    if exit_input==2:
        exit()
    if exit_input== 3:
        return ""
    if exit_input==4:
        pass_test=input("Enter the password or PRESS ctrl+v to access the secret information:\n")
        if pass_test==password:
            print("Password Matched")
            print("Secret information is: You are going to be an billlionare")
            return inpp()
        if pass_test!=password:
            print("Wrong password")
            
            return inpp()
    
while True:

    all_char = "abcdefghijklmnpqrstuvwxyz"+"0123456789"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"!@#$%^&*()"
    num=int(input("Enter the length for your password: "))
    password="".join(random.sample(all_char, num))
    print("Yor Password is:",password)
    pyperclip.copy(password)
    print("[Password copied to clipboard, PRESS ctrl+v to paste the password]")
    
    print(inpp())


# with duplicate characters
#import random
#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#lengthinput=int(input("Enter the length of password you want : "))
#for i in range(lengthinput):
#    p="".join(random.choices(s))
#    print(p,end="")


