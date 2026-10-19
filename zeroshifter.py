'''
# using sort method to shift all zeroes at last
a=[12,0,9,0,6,3]
n=len(a)
for i in range(0,n):
    a.sort(reverse=True)
print(a)
'''
# shifting all zeroes to last using conditionals statement
num=0
l=[]
n=int(input("enter no. of elements:"))
for i in range(0,n):
    l.append(int(input("enter element:")))
print(l)
for i in range(0,n):
    if l[i]!=0:
        l[num]=l[i]
        num+=1
for i in range(num,n):
    l[i]=0
print(l)




