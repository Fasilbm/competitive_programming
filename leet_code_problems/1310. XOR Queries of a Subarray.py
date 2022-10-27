class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        prefix=[arr[0] for i in range(len(arr))]
        for i in range(1,len(arr)):
            prefix[i]=prefix[i-1]^arr[i]
        for j in range(0,len(queries)):
            if queries[j][0]!=0:
                temp=prefix[queries[j][1]]^prefix[queries[j][0]-1]
                ans.append(temp)
            else:
                ans.append(prefix[queries[j][1]])
        return ans
    # Timpe Complexity O(n)
    # Space Complexity O(n)
    
