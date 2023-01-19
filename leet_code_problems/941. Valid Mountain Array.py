class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        tip=max(arr)
        pos=arr.index(tip)
        l=pos-1
        r=pos+1
        count=Counter(arr)
        if len(arr)<3:
            return False
        elif count[tip]>1:
            return False
        elif pos==len(arr)-1 or pos==0:
            return False
        while l>=0 and r<=len(arr)-1:
            if arr[l]<arr[l+1] and arr[r]<arr[r-1]:
                l-=1
                r+=1
            else:
                return False
        while l!=-1:
            if arr[l]<arr[l+1]:
                l-=1
            else:
                return False
        while r!=len(arr):
            if arr[r]<arr[r-1]:
                r+=1
            else:
                return False
        return True
       

