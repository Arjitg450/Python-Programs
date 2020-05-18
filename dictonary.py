data0={
"arjit":1,"akshat":2
}

data1={
"name":"arjit",
"age":19,
"subject":"python"
}
data2={
"name":"akshat",
"age":23,
"subject":"ml"
}
while True:
     inp0=input("enter name")
     if inp0=="arjit":
          inp=input("Ask about me\n")
          print(data1.get(inp,"Ask appropriate questions"))

     elif inp0=="akshat":
          inp=input("Ask about me\n")
          print(data2.get(inp,"Ask appropriate questions"))
     else:
          print("arjit or akshat?")

     
