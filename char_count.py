def char_count(text,char):
     count=0
     for c in text:
          if c==char:
               count+=1
     return count
while True:
     inp=input("enter the file name\n")
     inp1=input("enter the char whose rep value you want to know\n")
     inp2=str(inp1)
     with open(inp+".txt") as f:
          text=f.read()
     print("rep value :",char_count(text,inp2))
     print("total no of char :",len(text)-text.count("\n"))
     aa=(char_count(text,inp2)/(len(text)-text.count("\n")))
     bb=str(aa*100)
     print("percentage of",inp2,"in file named",inp,"is :",(bb) +"%")

