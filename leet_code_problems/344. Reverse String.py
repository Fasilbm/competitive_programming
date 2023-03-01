class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lp=0
        rp=len(s)-1
        while lp<rp:
            s[lp],s[rp]=s[rp],s[lp]
            lp+=1
            rp-=1
        # Time complexity O(n)
        # Space complexity O(1)
        
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def pointers(l,r):
            if l<r:

                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
                pointers(l,r)
            else:
                return s
                
        pointers(0,len(s)-1)
        
      

     



    
