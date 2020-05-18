#binary search program

def binarysearch(A,n,value):
    mid=n//2
    
    if n==1:
        if A[0]==value:
            return True
        else:
            return False
    else:
        if value==A[mid]:
            return True
        elif value<A[mid]:
            return binarysearch(A[0:mid],n//2,value)
        elif value>A[mid]:
            return binarysearch(A[mid::],n-n//2,value)
        

A=[2,4,6,7,8,9,10,11]
n=len(A)
print(binarysearch(A,n,1))
