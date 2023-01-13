class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range (len(strs[0])):
            col=[]
            for j in range(len(strs)):
                col.append(strs[j][i])

            if sorted(col)!=col:
                count+=1
        return count


                
