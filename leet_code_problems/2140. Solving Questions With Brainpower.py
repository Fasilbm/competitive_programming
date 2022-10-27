class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        ans=[0 for i in range(len(questions))]
        for i in range(len(questions)-1,-1,-1):
            next=i+questions[i][1]+1
            if next<len(questions):
                ans[i]=ans[next]+questions[i][0]
            else:
                ans[i]=questions[i][0]
            if i<len(questions)-1:
                ans[i]=max(ans[i],ans[i+1])
        
        return max(ans)
    # Time Complexity O(n)
    # Space Complexity O(n)
