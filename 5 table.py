a=4
b=1
c=1

while True:
     try:
     
          password = int(input("enter password"))
          if password==345:
               break
          
          
     except:
          print("wrong password")
          continue


while True:
     try:
          inp = int(input("enter the no. for its table\n\n\n"))
     except:
          print("enter an integer")
          continue
    
     
     while True:
          print(inp,"*",b,"=",inp * b)
          b+=1
          c=inp*b
          if c==11*inp:
               c=0
               b=1
               break

     
               
