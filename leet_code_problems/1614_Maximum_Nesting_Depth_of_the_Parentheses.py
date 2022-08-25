class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        current=0
        
        for i in s:
            if i=="(":
                current+=1
                if current>depth:
                    depth = current
            elif i==")":
                if current>0:
                    current-=1
                else:
                    return False
        if current!=0:
            return False
        return depth
    
                
             
        
