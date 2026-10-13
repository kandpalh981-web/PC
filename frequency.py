import array
def frequency(a):
    m=len(a)
    max_val=0
    b=int(input("enter no. of elements to find iteration: "))
    for i in range(m):
        if b==a[i]:
            max_val+=1
    print(max_val)

arr=[]
n=int(input("enter no. of elements:"))
for i in range(n):
    arr.append(int(input("enter element:")))
frequency(arr)

