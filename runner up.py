import array
mx=0
smax=0
arr=[11,91,55,12,99,23,20]
for i in arr:
    if i>mx:
        mx=i
for i in arr:
    if i>smax and i<mx :
        smax=i
print(smax)


