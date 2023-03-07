class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)

        r = sum(weights)

        count = 0

        while l <= r :

            Sum = 0
            count = 1
            mid = l + (r - l)//2

            for i in weights:

                Sum += i


                if Sum > mid :

                    count += 1

                    Sum = i    

            if count <= days :

                r = mid - 1

            else:

                l = mid + 1

        return l



