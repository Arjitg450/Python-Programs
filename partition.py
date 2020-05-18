
def partition(arr,l,r):
    p=arr[l]
    i=l+1
    for j in range(l+1,r+1):
        if arr[j]<=p:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[l],arr[i-1]=arr[i-1],arr[l]
    return (i-1)




def quicksort(arr,l,r):
    if l<r:


        pi=partition(arr,l,r)
        
        quicksort(arr,l,pi)

        quicksort(arr,pi+1,r)

    return arr


with open('H:\\qs.txt') as f:

    a = [[int(x) for x in ln.split()] for ln in f]
    data_set = []
    for ln in f:
        line = ln.split()
        if line:
            a = [int(x) for x in line]
            data_set.extend(a)
arr=data_set
r=len(arr)-1 #last element index
n=len(arr)
l=0
#r=index of last element


print(quicksort(arr,l,r))

