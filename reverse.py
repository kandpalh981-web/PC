'''
import array
#reverse using reverse method
arr=[]
n=int(input("enter no. of elements:"))
for i in range(n):
    arr.append(int(input("enter element:")))
for i in range(len(arr)):
  reversed_arr=arr[::-1]
print(reversed_arr)
'''
#reverse without reverse method
import array
arr=[]
b=[]
n=int(input("enter no. of elements:"))
for i in range(n):
    arr.append(int(input("enter element:")))
for i in range(len(arr)-1,-1,-1):
    b.append(arr[i])
print(b)


