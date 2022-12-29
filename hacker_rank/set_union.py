# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
English=set(map(int,input().split()))
m=int(input())
French=set(map(int,input().split()))

print(len(English.union(French)))
