class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        maxi = max(nums)
        mini = min(nums)
        return max(0, maxi-k-mini-k)
