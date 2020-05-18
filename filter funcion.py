def even_no(num):
    if num%2==0:
        return num



lis= range(0,101)
ab=list(filter(even_no,lis))
print(ab)
