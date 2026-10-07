def even_odd(num):
    even=[]
    odd=[]
    for i in num:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

num=[10,35,26,55,88,92,89]
even,odd=even_odd(num)
print("even numbers: ",even)
print("odd numbers: ",odd)