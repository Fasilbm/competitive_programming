class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap={}
        for i,c in enumerate(s):
            hashmap[c]=i
        res=[]
        size=0
        last=0
        for i,j in enumerate(s):
            size+=1
            last=max(last,hashmap[j])
            if last==i:
                res.append(size)
                size=0
        return res
            
        # Time Complexity O(n)
        # Space Complexity O(n)
            
            
        
        
       
