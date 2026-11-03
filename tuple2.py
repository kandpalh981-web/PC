# storing daily temperature in tuple
n=int(input("enter size of tuple: "))
num=[]
ad=0
count=0
for i in range(n):
    num.append(float(input("enter daily temp: ")))
    x=tuple(num)
print(x)
for j in range(n):
    ad=ad+x[j]
print(f"sum of daily temp is: {ad}")
avg=sum(num)/n
print(f"{avg:.2f} is the average temperature")
for i in range(n):
    if num[i]>avg:
        count=count+1
print(f"{count} days has above average temperature",)
