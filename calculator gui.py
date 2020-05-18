from tkinter import*
cal =Tk()
cal.geometry("500x500")#DEFINING THE SIZE OF WINDOW
cal.title("CALCULATOR")#TITLE OF THE WINDOW
callabel=Label(cal,text="CALCULATOR")#TITLE OF THE APPLICATION
callabel2=Label(cal,text="BY ARJIT GUPTA") #NAME OF THE CREATOR
callabel.pack(side=TOP)# TO SET PLACE FOR THE TITLE
callabel2.pack(side=BOTTOM) #TO PLACE CREATOR'S NAME AT THE BOTTOM OF CALCULATOR
textinput=StringVar()
operator=""

