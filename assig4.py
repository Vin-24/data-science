#1 WAP to print all elements of a list using a for loop. Take the elements of the list from the user.
"""
l=[]
n=int(input("how many element you want to add in list"))
for i in range(0,n):
    e=input("give element")
    l.append(e)
for s in l:
    print(s)
print(l) 
"""
#WAP to take inputs from user to make a list. Length of the list has to be taken from the user. Again take one input from user and search 
# it in the list and delete that element, if found. If not found, print "Element not present".
##For e.g. Input: len_list = 5
#                list = ["a", "b", "y", "e", "p"]
#                search_element = "g"
#                    Output: "Element not found"
#                search_element = "e"
#                    Output: ["a", "b", "y", "p"]  
"""
l=[]
n=int(input("how many element you want to add in list"))
for i in range(0,n):
    e=input("give element")
    l.append(e)
print(l)    
se=input("search element in the list")
if se in l:
    l.remove(se)
else:
    print("element not found")
    
print(l) 
"""

#Make a grading system for a school based on the marks of the students using the following criteria. 
#    Marks 0 - 40 : Grade F
#     41 - 50 : Grade E
#     51 - 70 : Grade D
#     71 - 80 : Grade C
#     81 - 90 : Grade B
#     91 - 100: Grade A
#Continuously take marks as input from the user and print the grade. 
#The user can enter "Stop" to stop the loop.
"""
while True:
    m=int(input("give marks\n"))
    if m<=40:            print("Grade 'F'\n")
    elif m>40 and m<=50: print("Grade 'E'\n")  
    elif m>50 and m<=70: print("Grade 'D'\n") 
    elif m>70 and m<=80: print("Grade 'C'\n") 
    elif m>80 and m<=90: print("Grade 'B'\n") 
    elif m>90 and m<=100:print("Grade 'A'\n") 
    else:                print("invalid input")
    give_marks=input("do you want to stop, 'y/n'\n").lower()
    if give_marks =='y':
        print("thank you")
        break
"""
# WAP to save the cube of all numbers from 1 to a number n in list, where n is taken as input from the user.
# For e.g. Input: 5
# Output: [1, 8, 27, 64, 125]  #Cube of numbers from 1 to 5 where 5 is the input from the user  
"""
l=[]
n=int(input("how many element you want to give to list")) 
for i in range(0,n):
    e=int(input("give elements"))
    l.append(e*e*e)
print(l)  
"""
# WAP to print even numbers in a given range in reverse order. Take the range from the user. 
# For e.g. Input: start = 3
#                   End = 14 
#         Output: 14, 12, 10, 8, 6, 4  
"""
s=int(input("give the start the range\n"))
e=int(input("give the ending range\n"))
for i in range(e,s,-1):
    if i%2==0:
        print(i)
"""
#L6  WAP to print odd numbers in a given range in reverse order. Take the range from the user. 
# For e.g. Input: start = 3 
#                 End = 14 
#         Output: 13, 11, 9, 7, 5, 3 
"""      
s=int(input("give the start the range\n"))
e=int(input("give the ending range\n"))
for i in range(e,s,-1):
    if i%2==1:
        print(i)   
"""        
#WAP to print the following pattern. e.g. i/p: n = 4 
#     o/p: 
#         1 
#         1 2 
#         1 2 3 
#         1 2 3 4
"""
n=int(input("give input"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 
"""
#Write a program to calculate the sum of series up to n terms for a digit d. n & d are taken as input from the user.
# For example:
#     Input: n = 5, d = 2
#     Logic: 2 + 22 + 222 + 2222 + 22222 
#     Output: 24690  
"""     
n = int(input("Enter the value of n\n "))
d = int(input("Enter the value of d\n "))

s = 0
for i in range(1, n+1):
    x= int(str(dAA) * i)
    s += x

print(s)
"""



#WAP that keeps on accepting numbers from the user until the user enters Zero(0) as input.  Display the sum and average of all the numbers. 
# For example: 
#     Input: 3, 6, 8, 2, 5, Stop 
#     Output: Sum = 24 
#             Average = 4.8
"""
sum = 0
count = 0
while True:
    n = int(input("Enter a number (enter 0 to exit): "))
    if n == 0:
        break
    sum += n
    count += 1
if count > 0:
    avg = sum / count
else:
    avg = 0
print(sum)
print(avg)
"""
# Accept n numbers from the user and display their average. n is input from the user. 
# For example: 
#     Input: n = 5 
#         Numbers = 3, 6, 2, 9, 0 
#     Output: Average = 4.0
"""
n=int(input("how many numbers younwant to take as a input\n"))
s=0
for i in range(0,n):
    nu=int(input("give numbers\n"))
    s+=nu
avg=s/n
print(s)
print(avg)
"""
#c-)||\ |(  
#)|\|| \|(_r
#string Questions

#S1 Write a Python program to count the number of each of the characters (character frequency) in a string input by the user. Ignore the case. 
#    For example: Input: "Python is great" 
# 		Output: P = 1, y = 1, t = 2, and so on... 
'''
n=input("enter string")
count={}
for i in n:
    if i in count:
        count[i]+=1
    else:count[i]=1
print(count)        
'''






















































##LIST QUESTION

# WAP to remove empty strings from the list of strings. Take list as input from the user. 
# For example: Input: ["My", "name", "", "is", "", "Alankrita", "", "."] 
#             Output: ["My", "name", "is", "Alankrita", "."]
"""
l=[]
n=int(input("how many element you want to add in list"))
for i in range(0,n):
    e=input("give element")
    l.append(e)
print(l) 
while "" in l:
    l.remove("") 
print(l)    
"""



#WAP to make a list of all the characters starting from character 'A' to the input character from the user. 
# For e.g. Input: 'H' 
#         Output: ["A", "B", "C", "D", "E", "F", "G", "H"]  
'''
n=input("enter the character").upper()
l=[]
for i in range(ord('A'),ord(n)+1):
    l.append(chr(i))
print(l)
'''
#WAP to check if a specific employee e is present in a company or not. Employee names are saved in a list. 
#e is taken as input from the user. 
# For example: empList = ["Ashwin", "Rachit", "Sanjana", "David", "Komal"] 
#             Input1: "Komal" 
#             Output1: "Employee is present" 
#              
#             Input2: "Harshil" 
#             Output2: "Employee is not present" 
"""
l = ["Ashwin", "Rachit", "Sanjana", "David", "Komal"]
n=input("enter the name you want to search")
print(l.index(n))
if n in l:print("employee is present")
else:     print("employee is not present")    
"""
#Write a python program to find the maximum and minimum number in a list of 10 elements  
# (taken as input from the user) and also find the index position of the these numbers. 
# For example: Input : [25, 2, 1, 86, 42, 32, 27, 12, 31, 10] 
# 	Output: Max Number: 86, Index of Max Number: 3 
# 		Min Number: 1, Index of Min Number: 2
"""
l=[]
n=10
for i in range(0,n):
    e=input("give element")
    l.append(e)
print(l)
a=min(l)  
b=max(l) 
print("min number:",a,"index of number is:",l.index(a))
print("max number:",b,"index of number is:",l.index(b))
"""
#Given two Python lists of same length. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order. 
#For example: Input = list1 = [10, 20, 30, 40] 
# 			list2 = [100, 200, 300, 400] 
#             Output: 10 400 
#                     20 300 
#                     30 200 
#                     40 100
"""
l=[]
n=int(input("how many element you want to add in list"))
for i in range(0,n):
    e=input("give element")
    l.append(e)
print(l)
for s in l:
    print(s)  
l2=l[::-1]
print(l2)
for s2 in l2:
    print(s2)
"""
#WAP to concatenate two lists index-wise.  
# list1 = ["M", "na", "i", "Ashu"]  
# list2 = ["y", "me", "s", "tosh"]  
#     Output: ['My', 'name', 'is', 'Ashutosh']
"""
l1 = ["M", "na", "i", "Ashu"]  
l2 = ["y", "me", "s", "tosh"] 
l3=[]
for i in range(min(len(l1),len(l2))):
    c= l1[i]+l2[i]
    print(c)
    l3.append(c)
print(l3)
"""
# WAP to remove/delete items from a list while iterating without creating a duplicate list. 
# Take the elements to be deleted from the user in real-time. 
"""
l=[]
n=int(input("how many element you want to add in list"))
for i in range(0,n):
    e=input("give element")
    l.append(e)
dele=input("input the item you want to delete from thr list")    
print(l)    
for s in l[:]:
    if str(s) in dele:
        l.remove(s)
print(l) 
"""
#WAP to generate a Python list of all the prime numbers between n to m where n & m are taken as input from the user.
"""
l=[]
n=int(input("enter the range1:\n")) 
m=int(input("enter the range 2:\n"))
for i in range(n,m):
    if i%2!=0:
        print(i)
        l.append(i)
print(l)
"""
# WAP to concatenate two lists in the following order: 
#     list1 = ["Hello ", "World"] 
#     list2 = ["Hi", "There"] 
#     Output: ['Hello Hi', 'Hello There', 'World Hi', 'World There']

# l1 = ["Hello ", "World"] 
# l2 = ["Hi", "There"] 
# l3=[]
# for i in range(min(len(l1),len(l2))):
#     c=l1[i]+l2[i]
#     l3.append(c)
# print(l3)    
"""
l1 = ["Hello ", "World"] 
l2 = ["Hi", "There"] 
l3=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        l3.append(l1[i]+''+l2[j])
print(l3)    
"""
#Li10
#Given two lists having names of students and their corrsponding marks.
#names = ["Ashutosh", "Ajay", "Alankrita", "Rachit", "Komal", "Anil"]
#marks = [23, 21, 26, 23, 27, 24]
#Take name of a student as input from the user and output his/her marks.

#For e.g.:
 #   Input1: "Alankrita"
  #  Output1: 26
        
   # Input2: "Someone"
    #Output2: "Student not found"
""" 
names = ["Ashutosh", "Ajay", "Alankrita", "Rachit", "Komal", "Anil"]
marks = [23, 21, 26, 23, 27, 24]
n = input("give the name of the student").title()
def add():
    add_new=input(" do you want to add the student, 'y/n'\n").lower()
    if add_new =='y':
        new_name=input("enter the new name")
        names.append(new_name)
        new_marks=int(input("enter the marks of the student"))
        marks.append(new_marks)
    

if n in names:
    x = names.index(n)
    print(names[x])
    print(marks[x])
    give_marks=input("do you want to update marks, 'y/n'\n").lower()
    if give_marks =='y':
        marks[x]=int(input("enter new marks"))
        print(marks[x])
        print(names)
        print(marks)    
else:
    print("invalid input")
    add()
"""
##DICTIONARY QUESTION    
#D1
#WAP in Python to merge following dictionaries to create a new one:
#	dic1={1:10, 2:20}
#	dic2={3:30, 4:40}
#	dic3={5:50, 6:60}
# Python code to merge dict using update() method
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

def Merge(dict1, dict2):
	return(dict2.update(dict1))
Merge(dic1,dic2)
print(dic2)
Merge(dic2,dic3)
print(dic3)
"""
         #or
# Python code to merge dict using a single
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
def Merge(dict1, dict2, dict3):
	res = {**dict1, **dict2, **dict3}
	return res
dic4 = Merge(dic1, dic2, dic3)
print(dic4)
"""
        #or
#by | method 
"""        
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
def Merge(dict1, dict2, dict3):
	res = dict1 | dict2 | dict3
	return res
dic4 = Merge(dic1, dic2, dic3)
print(dic4)
"""

#D2
#WAP in python to generate and print a dictionary that contains a number (between 1 and n) 
#in the form {x : x*x} where n is the input from the user.

#For e.g. Input: 4
 #       Output: {1:1, 2:4, 3:9, 4:16}
"""
d = {}
n=int(input("give the number"))

for i in range(1,n):
    #k = i
    #v = i*i

    d[i] = i*i
print(d)
"""

#D3
#WAP in python to find the number of vowels, consonants, digits, white space characters & 
#special characters in a string and save the result in the form of a dictionary.
"""
def string_count(s):
    counts = {
        'vowels': 0,
        'consonants': 0,
        'digits': 0,
        'whitespace': 0,
        'special': 0
    }
    for c in s:
        if c.isalpha():
            if c in 'aeiouAEIOU':
                counts['vowels'] += 1
            else:
                counts['consonants'] += 1
        elif c.isdigit():
            counts['digits'] += 1
        elif c.isspace():
            counts['whitespace'] += 1
        else:
            counts['special'] += 1
    
    return counts
n=input("give anything")
d=string_count(n)
print(d)
"""

#D4(doubt)
#WAP to reverse map the dictionary items. Take dictionary as input from the user.

#	For eg., Input: d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
 #           Output: d = {65: 'A', 66: 'B', 67: 'C', 68: 'D'}
"""
d = input("Enter a dictionary in the format {'key1': value1, 'key2': value2, ...}: ")

d = eval(d)

d = {value: key for key, value in d.items()}

print(d)
"""
#D5
#WAP to save Username and Password of 10 employees in an organisation. 
#Take the Username and Password as input from the user one by one and save in the Dictionary.
"""

ed = {}
n=int(input("enter the number of employee you want to store "))
for i in range(1,n):
    username = input(f"Enter username for employee {i+1}: ")
    password = input(f"Enter password for employee {i+1}: ")

    ed[username] = password
print(ed)
"""