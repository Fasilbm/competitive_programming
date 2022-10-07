class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels='a,e,i,o,u'
        res=[]
        count=0
        for i,char in enumerate(s):
            if char in vowels:
                count+=1
            if i-k>=0 and (s[i-k] in vowels):
                count-=1
            if i-k+1>=0:
                res.append(count)
        return max(res)
    # Time complexity O(n)
    # Space Complexity)O(n)
