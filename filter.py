while True:
     inp=input("enter the range :  ")
     inp1=int(inp)
     nums=[]
     for i in range(int(inp1)):
          i+=1
          nums.append(i)


     print(nums)
     inp2=input("odd or even  :")
     if inp2=="even":
          print(list(filter(lambda x:x%2==0,nums)))
     elif inp2=="odd":
          print(list(filter(lambda x:x%2!=0,nums)))
     else:
          print("choose btw odd or even")



