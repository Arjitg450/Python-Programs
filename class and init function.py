class records():
     def __init__(self,fname,lname,salary,expe):
          self.fname=fname
          self.lname=lname
          self.email=fname+"."+lname+"@fht.com"
          self.fullname=fname+lname
          self.salary=salary
          self.expe=expe
     def sname(self):
          return '{} {}'.format(self.fname[0],self.lname[0])

emp1=records('arjit','gupta','100000','2 yrs')
emp2=records('sushant','saxena','900000','2 yrs')

print(emp1.sname())

     
