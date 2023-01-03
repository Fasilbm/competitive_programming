# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input())
words=[]
for i in range(n):
    words.append(input())
count=Counter(words)
print(len(count))
for i in count.values():
    print(i,end=" ")
