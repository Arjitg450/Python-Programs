inp1=input("Enter first name\n")
inp2=input("Enter last name\n")



def add_surname(func):
     return func + inp2
def first_name(x):
     return str(x)


print(add_surname(first_name(inp1)))
