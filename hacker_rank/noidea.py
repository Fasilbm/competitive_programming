# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())

integer_list=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))

happiness=0

for val in range(len(integer_list)):
    if integer_list[val] in A:
        happiness+=1
    elif integer_list[val] in B:
        happiness-=1
    else:
        continue
print(happiness)


    
    

    
    
