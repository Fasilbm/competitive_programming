class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        new=[]
        for i in num:
            while k>0 and new and new[-1]>i:
                    k-=1
                    new.pop()
            new.append(i)
        new=new[:len(new)-k]
        new="".join(new)
        return str(int(new)) if new else "0"
    # Time Complexity O(n)
    # Space Complexity O(n)
