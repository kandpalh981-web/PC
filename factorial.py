def factorial(num):
    r=1
    for i in range(1,num+1):
        r=r*i
    return r

ans=factorial(int(input("enter the number: ")))
print(ans)