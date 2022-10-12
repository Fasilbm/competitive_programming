class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        l=1
        new=[]
        for i in nums:
            new.append(int(i))
        new.sort(reverse=True)
        while l<len(nums) and k>1:
                l+=1
                k-=1
        return str(new[l-1])
    # Time Complexity O(nlogn)
    # Space Complexity O(n)
