class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rp=len(numbers)-1
        lp=0
        length=len(numbers)
        while lp<rp:
            if numbers[lp]+numbers[rp]==target:
                numbers.append(lp+1)
                numbers.append(rp+1)
                break
            elif numbers[lp]+numbers[rp]<target:
                lp+=1
            else:
                rp-=1
        numbers.reverse()
        for j in range(length):
            numbers.pop()
        numbers.reverse()
        return numbers
    #Time complexity O(n)
    #Space complexity O(1)
        
