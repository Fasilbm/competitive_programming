class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_counter=Counter(arr)
        freq=sorted(arr_counter.values(),reverse=True)
        l=len(arr)//2
        p=0
        while l>0:
            l-=freq[p]
            p+=1
        return p
    # Yime complexity O(nlogn)
    # Space complexity (1)
    
       
