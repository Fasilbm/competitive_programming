class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        x=(bin(n))
        b=x[2:]
        p1=0
        p2=1
        if n==1:
            return True
        while p2!=len(b):
            if b[p1]==b[p2]:
                return False
            p1+=1
            p2+=1
        return True





        

