class Solution:
    def hIndex(self,citations) :

        l = 0

        r = len(citations) - 1

        res = -1

        while l <= r :

            mid = l + (r - l) // 2  

            if len(citations) - mid <= citations[mid]:

                res = mid

                r = mid - 1

            else :

                l = mid + 1

        return len(citations) - res if res != -1 else 0
