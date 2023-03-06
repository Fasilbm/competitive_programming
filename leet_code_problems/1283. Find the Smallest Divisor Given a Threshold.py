class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l = 1

        r = max(nums)

        while l <= r :

            mid = l + (r - l) // 2

            Sum = 0

            for i in nums:

                Sum += math.ceil(i/mid)

            if Sum > threshold :

                l = mid + 1

            else:

                r = mid - 1

        return l


      
