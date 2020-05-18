def partition(arr,start,end):
    pivot=arr[end-1]
    pindex=0
    for i in range(start,end-1):
        if arr[i]<=arr[end-1]:
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex+=1
    arr[end-1],arr[pindex]=arr[pindex],arr[end-1]
    return pindex



def quicksort(arr,start,end):
    if start>=end-1:
        return arr
    else:
        p=partition(arr,start,end)
        print(p)
        quicksort(arr,start,p)
        quicksort(arr,p+1,end)
        return arr


arr=[8,4,9,1,2,3]
start=0
end=len(arr)
quicksort(arr,start,end)
