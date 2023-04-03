class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        count=0
        while x or y:
            if (x&1==1 and y&1==0) or (y&1==1 and x&1==0) :
                count+=1
            x=x>>1
            y=y>>1
        return count
