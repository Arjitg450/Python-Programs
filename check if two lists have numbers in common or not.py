a=[1,6,3,7]
b= [1,7,6,4]
i=0
j=0
for nums in range(len(a)):
    for numss in range(len(b)):
        if b[j]==a[i]:
            print("yes b[",j,"] == a[",i,"]")
        else:
            print("no")
        
        if j==3:
            continue
        else:
            j=j+1
    i=i+1
    j=0
