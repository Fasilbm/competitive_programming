t=int(input())
for i in range(t):
    org=int(input())
    count=0
    if org==1:
        print(3)
        continue
    found=0
    num=org
    while not found:
        if ((num)&1==1):
            y=2**count
            found=1
        else:
            count+=1
            num=num>>1
    if y^org > 0:
        print(y)
    else:
        print(y+1)

