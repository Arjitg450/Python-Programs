line=0
word=0
character=0
inp = input("Enter the text\n")
for alll in inp:
    for words in alll:
        if words==" ":
            word=word+1
        for characters in words:
            character=character+1

print("Words :",word+1)
print("Character :",character)
    
