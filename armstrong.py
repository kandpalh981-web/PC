num=int(input("enter number:"))
og=num
ad=0
while num>0:
    digit=num%10
    ad+=digit**3
    num=num//10
if ad==og:
        print(f"{og} is a armstrong number")
else:
        print(f"{og} is not a armstrong number")