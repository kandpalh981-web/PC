import  array
'''
#sorting using sort method
arr=[]
n=int(input("enter no. of elements:"))
for i in range(n):
    arr.append(int(input("enter element:")))
for i in range(len(arr)):
    arr.sort()
print(arr)
'''

#sorting without sort methods using loops
#bubble sort
arr=[]
n=int(input("enter no. of elements:"))
for i in range(n):
    arr.append(int(input("enter element:")))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)

