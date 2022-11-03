class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans=[]
        def flip(end):
            start=0
            while start<end:
                A[start],A[end]=A[end],A[start]
                start+=1
                end-=1
        for i in range(len(A)-1,-1,-1):
            max=i
            for j in range(i,-1,-1):
                if A[j]>A[max]:
                    max=j
            if max!=i:
                flip(max)
                flip(i)
                ans.append(max+1)
                ans.append(i+1)
        return(ans)
   
