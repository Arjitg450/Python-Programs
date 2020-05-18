
     
     
          

while True:
     inp=input("enter the range :  ")
     inp1=int(inp)
     nums=[]
     for i in range(int(inp1)):
          i+=1
          nums.append(i)


     print(nums)
     inp2=input("odd/even/prime :")
     if inp2=="even":
          print(list(filter(lambda x:x%2==0,nums)))
     elif inp2=="odd":
          print(list(filter(lambda x:x%2!=0,nums)))
     elif inp2=="prime":
          lower=int(input("enter lower range: "))
          upper=int(input("enter upper range: "))

          for num in range(lower,upper+1):
               if num>1:
                    for i in range(2,num):
                         if num%i==0:
                              break
                    else:
                         print(num)
     else:
          print("choose btw odd or even")



