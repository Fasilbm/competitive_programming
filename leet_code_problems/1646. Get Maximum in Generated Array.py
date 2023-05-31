class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        arr = [0,1]
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(2,n+1):
            if i%2==0:
                arr.append(arr[i//2])
            else:
                x=(i-1)//2
                arr.append(arr[x]+arr[x+1])

        return max(arr)

