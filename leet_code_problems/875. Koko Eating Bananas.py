class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        res, r = float("inf"),max(piles)
        
        while l <= r :

            mid = l + (r - l) // 2

            count=0

            for i in (piles):

                count += math.ceil(i / mid)

            if count < h :

                r = mid - 1
                res = min(res,mid)

            elif count > h:

                l = mid + 1

            else:

                res = min(res,mid)
                r = mid - 1

        return res

    













