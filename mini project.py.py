#name: Ali Amin
#student ID:404130423
#Title: Advanced Programing Course mini project

import random

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

def get_number():
    """Getting a Number From the user """
    number=input("number:")

    if check_number(number) :
        return number 
    else:
        return get_number()

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

counter=0

def equal():
    """ main function"""

    number=product()
    global counter
    while True:
        user_number=get_number()
        if number==user_number:
            print("You won")
            return
            
        else:
            counter+=1
            print(f"count:{counter}")
            print("Try again!!")
            guidance(number,user_number)

        if counter>10:
            print(f"You lose and Correct number is {number}")
            return

def guidance(number,user_number):
    """help user find the number """

    for i in range(len(number)):
        for j in range(len(user_number)):
            if i==j:
                if number[i]==user_number[j]:
                    print(f" {number[i]} is Correct")

equal()