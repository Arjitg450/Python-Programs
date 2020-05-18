#overloading an operator

class total_no_of_seats():
    def __init__(self,no_of_seats):
        self.no_of_seats=no_of_seats
        
    def __add__(class1,class2):
        return(class1.no_of_seats + class2.no_of_seats)
        


class1=total_no_of_seats(16)
class2=total_no_of_seats(12)
print("total no of seats are :",class1+class2)

#-----------------------------------------------------------------------#

#overloading an operator

class total_no_of_connections():
    def __init__(self,no_of_connections):
        self.no_of_connections=no_of_connections
        
    def __add__(per1,per2):#here __add__ = multiply or read __add__ as "__multiply__"
        return(per1.no_of_connections * per2.no_of_connections)
        


per1=total_no_of_connections(4)
per1A=total_no_of_connections(6)
print("total no of connections of per1 are :",per1+per1A)





