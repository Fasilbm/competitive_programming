class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=str(x)
        l=0
        r=len(b)-1
        while l<=r:
            if b[l]==b[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        return True
