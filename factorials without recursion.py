
while True:
     num=int(input("enter the no whose factorial you want"))
     fact=1

     if num<1:
          print("no factorials exist")
     else: 
          for i in range(1,num+1):
               fact=fact*i
          print(fact)
