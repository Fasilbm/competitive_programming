class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        nums.sort()
        new=[]
        while len(nums)!=len(new):
            new.append(nums[l])
            l+=1
            if l<=r:
                new.append(nums[r])
                r-=1
        return new
    # YTime Complexity O(nlogn)
    # Space Complexity O(n)
     
