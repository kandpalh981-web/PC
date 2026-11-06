ad=0
num=int(input("enter number: "))
for i in range(1,num+1):
    if i==1 or i==2 or i%2==0:
        ad=ad+i
    else:
        ad=ad-i
print(ad)