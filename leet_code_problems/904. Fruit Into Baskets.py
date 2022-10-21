class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict=defaultdict(int)
        res=0
        l=0
        for r in range(len(fruits)):
            dict[fruits[r]]=1+dict.get(fruits[r],0)
            while len(dict)>2 and dict[fruits[l]]!=0:
                dict[fruits[l]]-=1
                if dict[fruits[l]]==0:
                    del dict[fruits[l]]
                l+=1
            res=max(res,r-l+1)
            r+=1
                
        return res
                
        # Time complexity O(n)
        # space complexity O(1)
        
        
        
      
