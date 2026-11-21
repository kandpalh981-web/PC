import numpy as np
arr=[]
n=int(input("enter the size of the array: "))
for i in range(n):
    arr.append(int(input()))
print(arr)
arr=np.array(arr)
print(arr.reshape(2,1))
