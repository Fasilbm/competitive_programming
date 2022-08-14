if __name__ == '__main__':
    n = int(input())
list=[]
while 1<=n<=20:
   n-=1
   list.append(n)
list.sort()
for i in list:
   print(pow((i),2))
