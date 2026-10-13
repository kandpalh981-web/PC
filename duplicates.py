import array
#remove duplicates elements using set
arr=[]
n=int(input("enter no. of elements:"))
for i in range(n):
    arr.append(int(input("enter element:")))
arr=set(arr)
print(arr)
