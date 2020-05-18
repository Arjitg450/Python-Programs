
def partition(arr,l,r):
    p=arr[l]
    i=l+1
    for j in range(l+1,r+1):

        if arr[j]<=p:
            
            
            
            arr[i],arr[j]=arr[j],arr[i]

            i+=1
    arr[l],arr[i-1]=arr[i-1],arr[l]
    return(i-1)




def quicksort(arr,l,r):
    n=len(arr)
    if l<r:
        

        pi=partition(arr,l,r)

        
        firstpart=quicksort(arr,l,pi)

       

        secondpart=quicksort(arr,pi+1,r)
    print(l+r+n-1)    
        




lineList = list()
with open('H:\\qss.txt') as f:
  for line in f:
    lineList.append(int(line.rstrip('\n')))

arr=lineList
arr[0],arr[-1]=arr[-1],arr[0]
r=len(arr)-1 #last element index
n=len(arr)
l=0
#r=index of last element

print(quicksort(arr,l,r))

