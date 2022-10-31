class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        count=0
        res=[]
        for i,j in points:
            mag=math.sqrt(i**2+j**2)
            ans.append([mag,(i,j)])
        ans.sort()
        for j in range(len(ans)):
            res.append(ans[j][1])
        return res[:k]
    # Time complexity O(nlogn + n)
    # Space Complexity O(n)
