import array
target=10
arr=[]
n=int(input("enter no. of elements:"))
for i in range(n):
    arr.append(int(input("enter element:")))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print([arr[i],arr[j]])

