from abc import ABCMeta, abstractmethod
from random import randint
class Account(metaclass=ABCMeta):
    @abstractmethod
    def CreateAccount():
        return 0
    @abstractmethod
    def Authenticate():
        return 0
    @abstractmethod
    def WithdrawMoney():
        return 0
    @abstractmethod
    def DepositMoney():
        return 0
    @abstractmethod
    def ShowBalance():
        return 0    
    
    


class SavingsAccount(Account):
    def __init__(self):
        self.savingsaccount={}
        #[key][0]=name,[key][1]=balance
    def CreateAccount(self,name,initialdeposit):
        print()
        self.accountnumber = randint[10000,99999]
        self.savingsaccount[self.accountnumber]=[name,initialdeposit]
        print("Your account is created.Your account no is ",self.savingsaccount[self.accountnumber])
    def Authenticate(self,name,accountnumber):
        if accountnumber in self.savingsaccount.keys():
            if name==self.savingsaccount[accountnumber][0]:
                print("Authetication successfull")
            else:
                print("Authetication failed")

    def WithdrawMoney(self,withdrawalamount):
        if withdrawalamount>self.savingsaccount[self.accountnumber][1]:
            print("Insufficient balance")
        else:
            print("Enter the amount you want to withdraw")
            self.savingsaccount[self.accountnumber][1]-=withdrawalamount
            print("Money successfuly withdrawal.Now Your balance is ",self.savingsaccount[self.accountnumber][1])
    def DepositMoney(self,depositmoney):
        print("Enter the amount of money you want deposit to your account")
        self.savingsaccount[self.accountnumber][1]+=depositmoney
    def ShowBalance(self):
        print(self.savingsaccount[self.accountnumber][1])

account=SavingsAccount()
print("Enrer 1 to create New Account")
print("Enter 2 to access an existing account")

userchoice=int(input())
if userchoice==1:
    print("Enter your name")
    name=input()
    print("Enter the initital deposit")
    deposit=int(input())
    account.CreateAccount(name,deposit)
elif userchoice==2:
    print("Enter the name")
    name=input()
    print("Enter the account number")
    accountnumber=int(input())
    account.Authenticate(name,accountnumber)
    print("enter 1 to withdraw money")
    print("enter 2 to deposit money")
    print("enter 3 to know your avialable balance")
    userchoicee=int(input())
    if userchoicee==1:
        withdrawalamount=int(input())
        account.WithdrawMoney(withdrawalamount)
    if userchoicee==2:
        depositmoney=int(input())
        account.DepositMoney(depositmoney)
    if userchoicee==2:
        account.ShowBalance()
        
    
    
    
    
    
    






        
        
                
            
        
        
