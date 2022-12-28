# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

my_dict=defaultdict(list)
n,m=map(int,input().split())

A=[]
B=[]

for i in range(n):
    A.append(input())
    
for j in range(m):
    B.append(input())
    
for indx, char in enumerate(A):
    my_dict[char].append(str(indx+1))

for val in B:
    if my_dict[val]:
         print(" ".join(my_dict[val]))
    else:
        print("-1")
    
   
    
        


    

    




