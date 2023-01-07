class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=i
        for j,k in operations:
            curr_index=hash_map[j]
            nums[curr_index]=k
            hash_map[k]=curr_index    
        return nums
