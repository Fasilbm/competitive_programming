# # # Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n=int(input())
result=[]
for i in range(n):
    ith_set=set(map(int, input().split()))
    if A.issuperset(ith_set):
        result.append(True)
    else:
        result.append(False)
print(all(result))
        
    

