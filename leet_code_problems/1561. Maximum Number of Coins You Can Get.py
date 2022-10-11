class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        p=1
        my_pick=[]
        for i in range(len(piles)//3):
            my_pick.append(piles[p])
            p+=2
        return sum(my_pick)
    # Time complexity O(nlogn)
    # Space complexity O(n)
