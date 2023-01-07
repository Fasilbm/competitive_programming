class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        rearranged=[]
        pos_ptr=0
        nega_ptr=0
        for i in nums:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)
        for j in range(len(nums)):
            if j%2==0:
                rearranged.append(positive[pos_ptr])
                pos_ptr+=1
            else:
                rearranged.append(negative[nega_ptr])
                nega_ptr+=1
        return rearranged
