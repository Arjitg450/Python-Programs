file = open("ssoo.txt","w")
file.write("hey its new")
file.close()

file=open("ssoo.txt","r")
print(file.read())
file.close()
