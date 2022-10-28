class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        ans=[]
        l_r=[0]
        r_l=[0 for i in range(len(security))]
        for i in range (1,len(security)):
            if security[i-1]>=security[i]:
                l_r.append(l_r[i-1]+1)
            else:
                l_r.append(0)
        for i in range (len(security)-2,-1,-1):
            if security[i]<=security[i+1]:
                r_l[i]=r_l[i+1]+1
            else:
                r_l[i]=0
        for k in range(len(security)):
            if l_r[k]>=time and r_l[k]>=time:
                   ans.append(k)
        return ans
    # Time Complexity O(n)
    # Space Complexity O(n)
