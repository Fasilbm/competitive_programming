class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        query=[]
        ans=[]
        for i in range(len(l)):
            query.append([l[i],r[i]])
        for i,j in query:
            temp=nums[i:j+1]
            temp.sort()
            diff=temp[1]-temp[0]
            count=0
            for k in range(len(temp)-1):
                 if temp[k+1]-temp[k]==diff:
                    count+=1
                 else:
                    ans.append(False)
                    break
            if count==j-i:
                ans.append(True)
        return ans
