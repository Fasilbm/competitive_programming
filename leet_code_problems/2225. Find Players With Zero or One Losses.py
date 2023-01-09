class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hash_map={}
        res1=[]
        res2=[]
        for i in matches:
            hash_map[i[0]]=0+hash_map.get(i[0],0)
            hash_map[i[1]]=1+hash_map.get(i[1],0)

        for j in hash_map:
            if hash_map[j]==1:
                res2.append(j)
            elif hash_map[j]==0:
                res1.append(j)
        res1.sort()
        res2.sort()
        final=[]
        final.append(res1)
        final.append(res2)
        return (final)
