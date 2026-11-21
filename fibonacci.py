def fib(num):
    ad=0
    a,b=0,1
    for i in range(1,num+1):
        print(a,end=" ")
        c=a+b
        a=b
        b=c

fib(int(input("Enter a number you want to print series: ")))
