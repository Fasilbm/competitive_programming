class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new=[[] for i in range(len(nums)+1)]
        res=[]
        numsHash={}
        for i in nums:
            numsHash[i]=1+numsHash.get(i,0)
        for i,j in numsHash.items():
            new[j].append(i)
        for i in range(len(nums),0,-1):
            for j in new[i]:
                res.append(j)
                if len(res)==k:
                    return res
        
        # Time complexity O(n)
        # Space Coplexity O(n)
            
        
