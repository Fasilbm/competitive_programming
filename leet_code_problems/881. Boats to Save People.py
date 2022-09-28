class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        lp=0
        rp=len(people)-1
        people.sort()
        while lp<=rp:
            count+=1
            if people[lp]+people[rp]<=limit:
                lp+=1
            rp-=1
        return count
    # Time complexity O(nlogn)
    # space complexity O(logn)
            
                
