#does array have duplicate entries
a=[1,2,3,4,5,1,7]
i=1
j=1
for num in a:
    for ab in range(len(a)):
        if num==a[i]:
            print("duplicate found! ",num,"is = a[",i,"]")
        else:
            print(num,"is not = a[",i,"]" )
        if i>4:
            break
        else:
            i=i+1
    i=0
                
