'''
count=0
num=int(input("enter number: "))
for i in range(1,num+1):
    if num%i==0:
       count+=1
if count==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
'''
'''
m=int(input("enter number: "))
n=int(input("enter power: "))
print(m**n)
'''

'''
num=int(input("enter number: "))
if num%2==0:
    print(True)
else:
    print(False)
'''
'''

ad=0
num=int(input("enter number: "))
for i in range(1,num+1):
    if i==1 or i==2 or i%2==0:
        ad=ad+i
    else:
        ad=ad-i
print(ad)
'''
'''
word="hello"
n=int(input("enter value of n: "))
match n:
    case 1:
       print(len(word))
    case 2:
        print(word.replace("l","j"))
    case 3:
        print(word.replace("l","",1))
    case 4:
        print(word.replace("l",""))
'''
'''
c=[]
a=input("enter first string: ")
b=input("enter second string: ")
for i in range(len(a)):
    for j in range(len(b)):
        if b[j]==a[i]:
           c.append(j)
print(c)
'''
'''
from numpy import *
n=int(input("enter value of n: "))
match n:
    case 1:
        a=ones(7 ,int)
        print(a)
    case 2:
        ar=array([11,65,66,44,76,50])
        print("maximum number:",ar.max())
        print("minimum number:",ar.min())
    case 3:
        ar=array([1,2,3,4,5])
        arr=array([1,4,7,8,9])
        print(ar*arr)
    case 4:
        ar=array([1,2,3,4,5,6])
        print(ar.reshape(2, 3))
'''
'''
t1=(1,2,3,4,5,6,7,8,9,10)
n=int(input("enter value of n: "))
match n:
    case 1:
        print(t1[:5])
        print(t1[5:])
    case 2:
        t2 = ()
        for i in t1:
            if i % 2 == 0:
                t2 = t2 + (i,)
        print("Even numbers tuple:", t2)
    case 3:
        t2=(11,12,13)
        t1 = t1 + t2
        print(t1)
    case 4:
        mx=0
        mini=0
        for i in t1:
            if i>mx:
                mx=i
        print("maximum in tuple",mx)
        for j in t1:
            if j<mini:
                mini=j
        print("minimum in tuple",mini)
'''