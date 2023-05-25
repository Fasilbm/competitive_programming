class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        count = defaultdict(int)
        for i in bills:
            if i == 5:
                count[i] += 1
            if i == 10:
                if count[5] >= 1 or 5*count[5]>=15:
                    count[5] -= 1
                    count[10] += 1
                else:
                    return False
            if i == 20:
                if count[10]>=1 and count[5]>=1:
                    count[5] -= 1
                    count[10] -= 1
                elif count[5]*5 >= 15:
                    count[5]-=3
                else:
                    return False
        return True
