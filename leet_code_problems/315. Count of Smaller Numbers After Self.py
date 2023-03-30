class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:


        counter=[[j,i] for i,j in enumerate(nums)]
        ans=[0 for i in range(len(nums))]
        def mergesort(left,right):

            if right-left==0:
                return [counter[left]]

            mid = left+(right-left)//2
            left_half=mergesort(left,mid)
            right_half=mergesort(mid+1,right)

            return merge(left_half,right_half)

        def merge(left_half,right_half):
            l=len(left_half)-1
            r=len(right_half)-1

            while l>=0 and r>=0:
                if left_half[l][0]>right_half[r][0]:
                    ans[left_half[l][1]]+=r+1
                    l-=1
                else:
                    r-=1
            l=0
            r=0
            merged=[]
            while l<len(left_half) and r<len(right_half):
                if left_half[l]<right_half[r]:
                    merged.append(left_half[l])
                    l+=1
                else:
                    merged.append(right_half[r])
                    r+=1

            merged.extend(left_half[l:])
            merged.extend(right_half[r:])

            return merged

        mergesort(0,len(counter)-1)

        return ans




       
