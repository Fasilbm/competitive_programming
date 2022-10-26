class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total=sum(chalk)
        k=k%total
        for i in range (len(chalk)):
            k=k-chalk[i]
            if k<0:
                return i
        # Time Complexity O(n)
        # Space Complexity O(1)
                
                
          
