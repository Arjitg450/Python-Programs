def fib(x):
    if x==2 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

for i in range(1,20):
    print(fib(i))

    
