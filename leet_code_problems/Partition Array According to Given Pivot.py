class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_and_equal=[]
        greater=[]
        pivots=[]
        for i in nums:
            if i < pivot:
                less_and_equal.append(i)
            elif i>pivot:
                greater.append(i)
            else:
                pivots.append(i)
        return less_and_equal+pivots+greater
