class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        prefix=[]
        strs.sort()
        left=strs[0]
        right=strs[-1]
        for i in range(min(len(left),len(right))):
            if left[i]==right[i]:
                prefix.append(left[i])
            else:
                return "".join(prefix)
        return "".join(prefix)
