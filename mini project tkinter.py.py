#name: Ali Amin
#student ID:404130423
#Title: Advanced Programing Course mini project

from tkinter import *  #Library Gui 
import random

def get_number():
    """Getting a Number From the user """
    number=number_entry.get()

    if check_number(number) :
        return number 
    else:
        msg_guid.insert("end","Invalid Number ! Try Again!\n")
        number_entry.delete(0,END)
        return 

def check_number(number):
    """check the number received from the user """
    if len(number)==4 :
        pass
    else:
        return False
        
    if number.isdigit():
        pass
    else:
        return False
        
    for i in number:
        if i < '1' or i > '6' :
            return False
        
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[i]==number[j]:
                return False
        
    return True

def product():
    """generate a random number """
    number=""
    while len(number) <4 :

        num=str(random.randrange(1,7))
        
        if num in number :
            pass
        else:
            number+=num 


    return number

def guidance(number,user_number):
    """help user find the number """

    for i in range(len(number)):
        for j in range(len(user_number)):
            if i==j:
                if number[i]==user_number[j]:
                    msg_guid.insert("end" , f" {number[i]} is Correct\n")
                    msg_guid.see(END)


number=product()
counter=0
status="Start"

def equal():
    """ main function"""
    global counter,status,number
    
    user_number=get_number()

    if user_number is None:
        return
    
    if number==user_number:
        status="Won"
        stat.config(text="status: {}".format(status), fg="green")
        return
            
    else:
        counter+=1
        num_cnt.config(text="count:{}".format(counter))
        status="Try again"
        stat.config(text="status: {}".format(status), fg="orange" )
        guidance(number,user_number)

    if counter>=10:
        status="lose"
        stat.config(text="status: {}".format(status) , fg="red")
        msg_guid.insert("end" , f"Correct Number is {number} \n")
        return

window=Tk()
window.title("Number Guessing")
window.geometry("500x400")

def config_tk():
    """ configure Label"""
    num_cnt.config(text="count:{}".format(counter))
    stat.config(text="status: {}".format(status))

Label(window,text="Enter Number:" , font=("Tahoma" , 15)).pack()
number_entry=Entry(window , width=27  )
number_entry.pack()


btn=Button(window)
btn.configure(text="ENTER", width=22 ,command=equal)
btn.pack()

frame=Frame(window)
frame.pack()

num_cnt=Label(frame ,text="count:")
stat=Label(frame ,text="status:")
num_cnt.pack(side="left" , padx=10)
stat.pack(side="left",padx=10)

config_tk()

msg_guid=Text(window )
msg_guid.configure(width=35 , height=15, bg="gray",pady=10)
msg_guid.pack()


window.mainloop()