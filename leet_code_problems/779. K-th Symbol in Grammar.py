class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1: return 0
        parent=self.kthGrammar(n-1,ceil(k/2))
        odd=(k%2==1)
        if parent==1:
            return 1 if odd else 0
        elif parent==0:
            return 0 if odd else 1
        
        
        #Timecomplexity O(nlogk)
        #Spacecomlexity O(n)
            
            
