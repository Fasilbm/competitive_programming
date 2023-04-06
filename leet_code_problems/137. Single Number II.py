class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ones=0
        twice=0
        for i in nums:
            ones^=i&~twice
            twice^=i&~ones
        return ones

