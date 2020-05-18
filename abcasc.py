def char_count(text,char):
     count=0
     for c in text:
          if c==char:
               count+=1
     return count

inp=input("enter the file name\n")
while True:
     inp2=input("enter the char whose repetetion value you want to know \n")
     inp3=str(inp2)
     with open(inp+"."+"txt") as f:
          text=f.read()
          print(char_count(text,inp3))
          print((char_count(text,inp3)/len(text)*100))

