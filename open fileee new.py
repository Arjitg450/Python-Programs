
with open("abcd.txt") as newfile:
     text = newfile.read()
     print(text)

     count=0
     if "c" in text:
          count+=1
          print(count)
     

