import random#for generating a random five digit number which acts a account number
class savingsaccount():
    def new_account(self,name,deposit,account_no):
        self.name=name
        self.deposit=deposit
        self.account_no=account_no
        
        print("Mr/mrs {} your account no is : {}".format(self.name,self.account_no))

        
            
        print("You have {} INR in your account".format(self.deposit))


class final_balance():
    def __init__(self,balance):
        self.balance=balance
        
            

class check_balance(final_balance):
    
    def check_balance(self,deposited):
        print("Enter the Name of Your account")
        check_name=input()
        if check_name==name:
            print("Enter your account no")
            check_account_no=input()
            if check_account_no==str(account_no):
                print("Your balance is {}".format(deposited))
                print(deposited)
                print("your new balance is {}".format(balance))
            else:
                print("wrong account no")

class withdraw_money(check_balance): 
                

    def withdraw_money(self,deposited):
        self.deposited=deposited
        
        print("Enter the Name of Your account")
        check_name=input()
        if check_name==name:
            print("Enter your account no")
            check_account_no=input()
            if check_account_no==str(account_no):
                print("Your balance is{}".format(deposited))
                
                
                
                
            else:
                print("wrong account no")
            print("Enter the amount you want to withdraw from your account")
            entered_amount=int(input())
            print("Now your balance is INR :")
            deposited=(int(self.deposited)-entered_amount)
            print(deposited)
            print("{} INR Money deducted from your account".format(entered_amount))
            print("Now your account balance is {}".format(deposited))
            deposit=deposited
            balance=deposited
            account=final_balance(balance)
            

class deposit_money(withdraw_money):


    def deposit_money(self,deposited):
        self.deposited=deposited
        print("Enter the Name of Your account")
        check_name=input()
        if check_name==name:
            print("Enter your account no")
            check_account_no=input()
            if check_account_no==str(account_no):
                print("Your balance is {}".format(deposited))
                
            else:
                print("wrong account no")
            print("Enter the amount you want to add to your account")
            entered_amount=int(input())
            deposited=(int(deposited) + entered_amount)
            print(deposited)
            print("Money successfully added to your account.")
            print("Now your account balance is {}".format(deposited))
            deposited=(int(deposited) + entered_amount)
            deposit=balance
             


while True:

    print("Enter 1 to create a new account")
    print("Enter 2 to access a existing account account ")
    
    
    userinp=int(input())
    if userinp==1:
        
        print("Enter a name for the account")
        name=input("")
        print("Enter initial amount you want to deposit")
        deposit=input("")
        for x in range(1):
            account_no=(random.randint(11111,99999))
            print(account_no)
            deposited=deposit
            balance=deposit 
        account=savingsaccount()
        account.new_account(name,deposit,account_no)


   
        
    elif userinp==2:
        
        
        
        print("press 1 to check your balance")
        print("press 2 to withdraw money from your account")
        print("press 3 for depositing money")
        deposited=deposit
        userinp_ea=int(input())
        if userinp_ea==1:
            account=check_balance()
            account.check_balance(deposited)
        if userinp_ea==2:
            account=withdraw_money()
            account.withdraw_money(deposited)
        if userinp_ea==3:
            account=deposit_money()
            account.deposit_money(deposited)


        

    

    
