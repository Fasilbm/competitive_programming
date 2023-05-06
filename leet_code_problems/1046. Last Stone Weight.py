class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def heapify(arr, n, i):
            minimum=i
            while True:
                left=2*i+1
                right=2*i+2
                if left<=n and arr[left]<arr[minimum]:
                    minimum=left
                if right<=n and arr[minimum]>arr[right]:
                    minimum=right
                if minimum != i:
                    arr[i],arr[minimum]=arr[minimum],arr[i]
                    heapify(arr,n,minimum)
                    return
                else:
                    return

        def HeapSort(arr, n):
            heapq.heapify(stones)
            n=len(arr)-1
            while n>=1:
                arr[0],arr[n]=arr[n],arr[0]
                heapify(arr,n-1,0)
                n-=1

        while len(stones)>1:
            HeapSort(stones,len(stones))
            stones=list(reversed(stones))
            if stones[-1]>stones[-2]:
                stones[-1]=stones[-1]-stones[-2]
                stones[-1],stones[-2]=stones[-2],stones[-1]
                stones.pop()
            else:
                stones.pop()
                stones.pop()
        return heappop(stones) if stones else 0
