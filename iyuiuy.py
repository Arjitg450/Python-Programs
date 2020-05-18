lineList = list()
with open('H:\\q2.txt') as f:
  for line in f:
    lineList.append(int(line.rstrip('\n')))
print(sum(lineList))
