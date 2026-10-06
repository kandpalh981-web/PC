#Tuple from user
n=int(input("enter size of tuple: "))
num=[]
for i in range(n):
    num.append(int(input("enter number: ")))
    x=tuple(num)
print(x)

# nested tuple from user

n=int(input("enter size of tuple: "))
num=[]
for i in range(n):
   x=int(input("press 1 for simple tuple & 2 fpr nested tuple: "))
   if x==1:
       num.append(int(input("enter number: ")))
       y=tuple(num)
   elif x==2:
       num2=[]
       m=int(input("enter size of tuple: "))
       for j in range(m):
           num2.append(int(input("enter number: ")))
       z=tuple(num2)
       num.append(z)
result=tuple(num)
print(result)
