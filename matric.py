matrix=[[1,4,7,3],[12,63,43,65],[12,55,22,77]]

for i in range(4):
    lst=[]
    for row in matrix:
        print(row[i])

transposed=[[row[i] for row in matrix] for i in range(4)]
print(transposed)
