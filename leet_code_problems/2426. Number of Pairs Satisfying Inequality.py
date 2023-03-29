
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.count1=0
        nums=[]
        for i in range(len(nums1)):
            nums.append(nums1[i]-nums2[i])

        def mergeSort(left, right):
            if left == right:
                return [nums[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1, right)
        
            return merge(left_half, right_half)


        def merge(left_half,right_half):
            merged=[]
            count=0

            l=0
            r=0
            while l<len(left_half) and r<len(right_half):
                if left_half[l]<=right_half[r]+diff:
                    count+=len(right_half)-r
                    l+=1
                    
                else:
                    r+=1  
            self.count1+=count
            l=0
            r=0

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

        (mergeSort(0,len(nums)-1))
        return (self.count1)

                



