#1WAP to display the last digit of a number. Take number as input. (Don't use indexing for this)
"""num=int(input("enter thr number"))
l=num%10
print("the last digit is",l)"""

#2Display all the numbers that are divisible by 5 from a list, l = [95, 52, -410, 57, 55, 10. -85,740, 81]
"""a = [95, 52, -410, 57, 55, 10. -85, 740, 81]
for i in  a:
    if(i%5==0):
        print(i)"""
#3WAP to calculate the count of elements in a string taken as input from the user:
"""x=input("enter anything") 
print(len(x))   """

#4WAP to check if a number is even or odd where number is taken as input:
"""x=int(input("enter number"))
if(x%2==0):
    print("the number is even")
else:
    print("the number is odd")"""
#5WAP to print astring in reverse order. Take the string as input from the user.
"""x=input("write anything")
r=x[::-1]
print(r) """   

#6WAP to check if 3rd last digit ofa number, taken as input, is divisible by 7 or not.

"""x=(input("write  number"))
l=int(x[-3])
if(int(x)<100):
    print("give greater number")
elif(l%7==0):
    print("divisible by 7")
else:
    print("not divisible by 7")"""    

#7Print characters from a string that are present at an even index number :
"""x=input("write anything")
n=x[0::2]
print(n)    """

#8Check if the first and last number of a list is the same
"""x=input("enter anything") 
if(x[0]==x[-1]):
    print("yes")
else:
    print("no") """

#9Calculate income tax for the input income by adhering to the Indian rules
"""x=int(input("enter your salary"))
t=0
if(x<250000):
    print("no tax")
if(x>250000 and x<500000):
    t=50000
    print(t)
elif(x>500000 and x<100000):
    t=100000
    print(t)  """

#10Write a Python program to check whether a string starts with vowel or not.
"""x=input("write anything\n")
v=["a","e","i","o","u"]
if x[0].lower() in v:
    print(True)
else:
    print(False)  """  

#11Write a Python program to check if all the characters of a string are vowel or not.
"""x=input("write anything\n")
v=["a","e","i","o","u"]
for i in x.lower():
    if i in v:
        print(True)
    else:
         print(False)   """

#12WAP to calculate percentage of a student through 5 subjects
"""sub1=int(input("give marks1\n"))
sub2=int(input("give marks2\n"))
sub3=int(input("give marks3\n"))
sub4=int(input("give marks4\n"))
sub5=int(input("give marks5\n"))
t=sub1+sub2+sub3+sub4+sub5
print(t/5)"""

#13WAP to convert '95.3' taken as input from the user into float value.
"""x='95.3'
print(float(x))"""

#14WAP to count the number of zeroes present in a number taken as input from the user.
"""x=int(input("give number"))
z=str(x)
count = z.count('0')
print(count)"""

#15WAP to calculate the surface area of a triangle. Take the required values as input
"""b = float(input("Enter the base of the triangle:\n "))
h = float(input("Enter the height of the triangle:\n "))
area = 0.5 * b * h
print(area)"""

#16WAP to accept day number from a user and print the day. For example, if input = 1 output = Monday
"""day = int(input("enter number"))
if day == 1:
    print("monday")
elif day == 2:
     print("tuesday")
elif day == 3:
    print("wednesday")    
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")  
elif day == 7:
    print("sunday")
else:
    print("invalid number")"""

#17WAP to check whether a person is eligible to vote or not based on their age
"""age=int(input("enter your age"))
if age>18:
    print("you cabn vote")
elif age<18:
    print("you cannot vote") 
else:
    print("try again") """      

#18Take n numbers from a user. Print their sum. Take n as input from the user
"""n = int(input("Enter the number\n "))
sum = 0
for i in range(n):
    num = float(input("Enter number : "))
    sum += num
print(sum)"""

#19WAP to print the square of all the even numbers in range. Take the range from the user.
"""s = int(input("Enter the starting number: "))
e = int(input("Enter the ending number: "))
for n in range(s, e+1):
    if n % 2 == 0:
        print(n**2)"""

#20Write a Python program to find the sum of the first n positive integers. Take n as input from the user.
"""n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)"""




    


   








