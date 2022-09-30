import math
n,m,a = map(int,input().split())
width = math.ceil(n/a)
Height = math.ceil(m/a)
print(int(height*width))
