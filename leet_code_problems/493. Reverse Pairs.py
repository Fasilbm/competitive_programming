class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        self.count1=0
        def mergeSort(left,right):

            if left-right==0:
                
                return [nums[left]]

            mid=left+(right-left)//2
            left_half=mergeSort(left,mid)
            right_half=mergeSort(mid+1,right)

            return merge(left_half,right_half)


        def merge(left_half,right_half):

            l=0
            r=0
            count=0
            while l<len(left_half) and r<len(right_half):
                if left_half[l]>right_half[r]*2:
                    r+=1
                else:
                    self.count1+=r
                    l+=1
            if l<len(left_half) and r>=len(right_half):
                self.count1+=r*(len(left_half)-l)
                
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


        mergeSort(0,len(nums)-1)

        return self.count1
