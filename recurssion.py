x=(int(input("enter the no whose factorial  you want")))
def factorials(x):
     if x==1:
          return 1
     else:
          return x*factorials(x-1)

print(factorials(x))



     
     
