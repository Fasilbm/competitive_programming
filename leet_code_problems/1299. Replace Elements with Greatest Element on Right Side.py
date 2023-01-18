class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new_max=arr[len(arr)-1]
        arr[len(arr)-1]=-1
        for i in range(len(arr)-2,-1,-1):
            curr=arr[i]
            new_max=max(new_max,arr[i+1])
            arr[i]=new_max 
            new_max=max(new_max,curr)
        return arr


