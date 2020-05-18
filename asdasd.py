markslist=[]
noofstudents = int(input("Enter the no of students"))
for marks in  range(noofstudents):
    marksos = int(input("Enter their marks"))
    markslist.append(marksos)
    
nm=0
print(markslist)
newlist=[]
for sm in markslist:
    nm=sm
    if sm>=37 and sm%5==0:
        newlist.append(sm)
    elif sm>37 and sm%5!=0:
        while sm%5!=0:

            sm=sm+1
        if sm%5==0 and sm-nm<3:
            newlist.append(sm)
            continue
    
            
        
        else:
            newlist.append(nm)
    elif sm<38:
        newlist.append(sm)
    
        
print(newlist)
        
    
