print("Hello, Welcome to my Project, Happy Learning")
 #Expected Output:
 #Hello, Welcome to my Project, Happy Learning

a="John"
b="Jim"
c="India"
print("Hello",a,"&",b,"Welcome to",c)
#Expected Output:
#Hello John & Jim Welcome to India

#Declare variables and assign values
a=5
b=4
c=8
print(a*b/c*b)
#Expected Output:  10.00

#Conditional Statements
a=5
if a>5:
    print("a is greater")
elif a<5:
    print("5 is greater")
else:
    print("a is equal to 5")
print("End of conditional statements")

#defining a function called first
def first():
    i=[1,2,3,4,5]
    for each in i:
        print("Hello, I'm",each)

def second(): #defining a function called second
    j=[6,7,8,9,10]
    for every in j:
        print("Hello, I'm",every)

def third(): #defining a function called third
    k=11
    while k<=15:
        print("Hello, I'm",k)
        k=k+1
def fourth(): #defining a function called fourth
    l=16
    while l<=20:
        print("Hello, I'm",l)
        l=l+1


print("Hi, Im numbers")
first()    #call the function by it's name
second()   #call the function by it's name
third()    #call the function by it's name
fourth()   #call the function by it's name
print("End of numbers")


# basic "for loop using range" programs
for i in range (6):
    print(i)

#basic "for loop using range mentioned" programs
for i in range(2,6):
    print(i)

#basic "for loop using range with increment" programs
for i in range(2,30,3):
    print(i)

#difference between break and continue using for loop

#1.break
a=["Pizza","Burger","Fries"]
for i in a:
    if i=="Burger":
        break
    print(i)
#Expected Output:
# Pizza

#2.Continue
a=["Pizza","Burger","Fries"]
for i in a:
    a=="Burger"
    continue
print(i)

#Expected Output:
#Pizza
#Fries
