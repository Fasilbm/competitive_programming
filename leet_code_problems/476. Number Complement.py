class Solution:
    def findComplement(self, num: int) -> int:

        summ=0
        j=0
        while num!=0:
            if num & 1 ==0:
                summ+=2**j
            j+=1
            num=num>>1
            
        return summ
