def infinite_5():
     while True:
          yield (5)

for i in infinite_5():
     print(i)
          
