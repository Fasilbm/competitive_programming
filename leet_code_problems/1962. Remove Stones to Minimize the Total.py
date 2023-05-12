class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        for i in range(len(piles)):
            piles[i]*=-1
        heapify(piles)
        for i in range(k):
            x=heappop(piles)
            y=-1*(-1*x-(math.floor((-1*x)/2)))
            heappush(piles,y)
        for i in range(len(piles)):
            piles[i]*=-1
        
        return sum(piles)

        
