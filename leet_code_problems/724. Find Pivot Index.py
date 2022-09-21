class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot=[]
        pref=[0]*len(nums)
        left=0
        right=0
        for j in range(1,len(nums)+1):
            pref[j-1]=nums[j-1]+pref[j-2]
        for i in range(0,len(nums)):
            if i==0 and (left==pref[len(nums)-1]-pref[0]):
                pivot.append(i)
                continue
            elif i==len(nums)-1 and (right==pref[i-1]):
                pivot.append(i)
                continue
            elif i!=0 and (pref[i-1]==pref[len(nums)-1]-pref[i]):
                pivot.append(i)
                continue
        if not pivot:
            return -1
        else:
            return pivot[0]
            
