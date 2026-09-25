import math
def calculates_the_area_of_a_circle():
    r=float(input("enter circle radius: "))
    circle_area=round(math.pi * math.pow(r, 2), 1)
    print("Circle area:",round(circle_area,1))

def converts_C_into_F():
    C=int(input("enter the temparature in celsius: "))
    F=float(C*9/5)+32
    print("{0} (C) = {1} (F)".format(C,F))

def check_prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True 

def check_number_is_perfect(n):
    if n<0:
        print("please enter a positive number!")
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return n==sum

def favorite_color(my_color):
    list_color=["Red","Yellow","White","Orange","Blue","Brown","Black"]
    my_color_formatted = my_color.strip().capitalize() 
    if my_color_formatted in list_color:
        idx = list_color.index(my_color_formatted)
        print("Your color is at index {0} in my list".format(idx+1)) 
    else:
        print("Sorry, I could not find your color")

def sequence():
    range1=list(range(0,7,1))
    range2=list(range(1,11,3))
    range3=list(range(5,0,-1))
    range4=list(range(6,-3,-2))
    print("range1", ", ".join(map(str, range1)))
    print("range2", ", ".join(map(str, range2)))
    print("range3", ", ".join(map(str, range3)))
    print("range4", ", ".join(map(str, range4)))  

def remove_dollar_sign(string):
    original_str=string.replace("$"," ")
    print(original_str)
    s=str(input("takes 1 parameter:"))
    newstr=s+original_str
    print(newstr)

def extracts_even(my_list):
    new_list=[]
    for item in my_list:
        if item%2==0:
            new_list.append(item)
    print(new_list)

def factorial(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    print("actorial of {0} is {1}".format(n,sum))

def divisors():
    divisors_of_number=[]
    n=int(input("enter a number: "))
    for i in range(1,n+1):
        if n%i==0:
            divisors_of_number.append(i)
    print(divisors_of_number)

def distanse_two_point():
    x1=float(input("enter x1: "))
    y1=float(input("enter y1:"))
    x2=float(input("enter x2: "))
    y2=float(input("enter y2: "))
    distance=round(math.sqrt(pow((x2-x1),2)+math.pow((y2-y1),2)),2)
    print("distane of ({0},{1}) and ({2},{3}) is {4})".format(x1,y1,x2,y2,distance))

def print_mxn():
    m=int(input())
    n=int(input())
    for i in range(m):
        for j in range(n):
            if i==0 or i==m-1 or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

while True:
    choise=int(input("Choise of your:"))
    if choise==1:
        calculates_the_area_of_a_circle()

    elif choise==2:
        converts_C_into_F()

    elif choise==3:
        n=int(input("enter a number"))
        if check_prime(n):
            print("{0} is a prime number".format(n))
        else:
            print("{0} is a not prime number".format(n))

    elif choise==4:
        n=int(input("enter a number: "))
        if check_number_is_perfect(n):
            print("{0} is a perfect number".format(n))
        else:
            print("{0} is a not perfect number".format(n))

    elif choise==5:
        color=str(input("What is your favorite color: "))
        favorite_color(color)

    elif choise==6:
        sequence()

    elif choise==7:
        n=str(input("enter a string: "))
        remove_dollar_sign(n)

    elif choise==8:
        my_list=[]
        n=int(input("enter number list: "))
        for i in range(n):
            value=int(input("value {0} of list: ".format(i+1)))
            my_list.append(value)
        print(my_list)
        extracts_even(my_list)

    elif choise==9:
        while True:
                try:
                    n=int(input("enter a number:"))
                    if n<0:
                        print("please enter a positive number:")
                        continue
                    factorial(n)
                except ValueError:
                    print("Invalid value please agian!")

    elif choise==10:
        divisors()

    elif choise==11:
        distanse_two_point()

    elif choise==12:
        print_mxn()