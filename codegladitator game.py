while True:
    try:
        T=int(input("enter the no of games. Must be between 1 to 10"))
        print("Ok. Now Hero's strength values")
        break
    except:
        print("No. of games must be between 1 to 10")
        
N=T

villanstren=[]
herostren=[]
a=1
b=1
while len(herostren)< T:
    print("Enter hero ",a," strength value")
    herosinp=input()
    herostren.append(herosinp)
    a+=1
print(herostren)

print("Now enter Villan's Strength values")
while len(villanstren)< T:
    print("Enter villan ",b," strength value")
    villansinp=input()
    villanstren.append(villansinp)
    b+=1
print(villanstren)
c=0
for test in range(T):
    if herostren[c]>villanstren[c]:
        print("Win")
    else:
        print("lose")

    c+=1
