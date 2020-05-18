def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        global count
        count+=len(x)-1
        if count>2*len(x):
            print(count)
        bb=first_part + second_part
    
        return bb
        

alist = [7,1,3,8,7,10,12,15,78,12,34,234,234,3,534,523,432,423,4]
count=0

print(quicksort(alist))

