t = int(input())

for i in range(t):
    
    n = list(map(int,input().split()))
    a = n[0]
    b = n[1]
        
    print(min(a,b,(a+b)//4))
    
