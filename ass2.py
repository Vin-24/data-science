#WAP to input a year in YYYY format and check whether it is a leap year or not
"""
x=int(input("give year"))
if(x%4 == 0 or x%400==0):
    print("leap year")
else:
    print("not a leap year")
"""


#Given an integer, n, perform the following conditional actions: If n is odd,
# print Weird If n is even and in the inclusive range of 2 to 5, print Not Weird If n is even and in the inclusive range of 6 to 20, print
#Weird If n is even and greater than 20, print Not Weird 
"""
n=int(input("give input"))
if(n%2==1):
    print("wierd")
else:
    if(n%2==0 and n>=2 and n<=5):
        print("not wierd")
    if(n%2==0 and n>=6 and n<=20):
        print("wierd")
    if(n%2==0 and n>20):
        print("wierd")   
"""

#WAP to count the occurence of even number and odd number between the range taken as input from the user. Hint: Range 10,55
#Expected Output Even number counts is 23 Odd number counts is 22 
"""
e= int(input("enter starting range"))
o= int(input("enter ending range"))
count_even=0
count_odd=0
for i in range(e,o):
    if i%2==0:
        count_even+=1
    else: count_odd+=1
print(count_even) 
print(count_odd)    
"""   

#WAP in Python to print square of numbers ranging from 1 to 25 but excluding numbers which are multiples of 5
"""
l=[]
for i in range(1,26):
    if i%5 != 0:
        l.append(i*i)
    else: continue   
print(l) 
"""

# WAP to replace the surnames of people in a list with their surname initia
#inputList = ['Deepak Sharma', 'Mohit Khurana', 'Dimple Kapadia', 'Archana Chawla']
"""
l=['Deepak Sharma', 'Mohit Khurana', 'Dimple Kapadia', 'Archana Chawla']
for i in range(len(l)):
    f,n=l[i].split(" ")
    l[i]= f+' '+n[0]+'.'
print(l)    
"""
#. WAP to display the first n multiples of d. Hint: input: n = 4, d = 6 output: 6, 12, 18, 24 
"""
n=int(input("enter number"))
d=int(input("enter the number"))
for i in range(1,n+1):
    x=i*d
    print(x)    
"""
# WAP to fetch only even values from a dictionary. Hint: dic = {‘val1’:10, ‘val2’:20, ‘val3’:23, ‘val4’:22 } Expected output: 10, 20, 22   
"""
d = {"val1":10, "val2":20, "val3":23, "val4":22 }
for i in d.values():
    if i%2==0:
      print(i) 
"""
#. WAP to convert lower letter to upper and upper letter to lower in a string. Hint: Input: PrOgRaMM Result is: pRoGrAmm 
"""  
s="PrOgRaMM"
n=""
for i in s:
    if i.islower():
        n+=i.upper()
    elif i.isupper():
        n+=i.lower()
    else:n+= i   

print(n)  
"""
# WAP in Python to count lower, upper, numeric and special characters in astring. Hint Input: @pyThOnlobb!Y34 Expected output Numeric counts 2 Lower counts 8 Upper
#counts 3 Special counts 
"""      
s=input("give input")
lower_count=0
upper_count=0
numeric_count=0
special_count=0
for c in s:
    if c.islower():
        lower_count +=1
    elif c.isupper():
        upper_count +=1
    elif c.isnumeric():
        numeric_count +=1
    else:
        special_count +=1
print("numeric count", numeric_count) 
print("lower count", lower_count) 
print("upper count", upper_count) 
print("special count", special_count) 
"""

 





 