from functools import reduce
def add_no(x,y):
    return x+y

lis=[1,2,3,4]
addlis=(reduce(add_no,lis))
print(addlis)
