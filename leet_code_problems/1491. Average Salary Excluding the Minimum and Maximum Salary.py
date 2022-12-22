class Solution:
    def average(self, salary: List[int]) -> float:

        # salary.sort()
        # left=0
        # right=len(salary)-1
        # average=(sum(salary)-salary[left]-salary[right])/(len(salary)-2)
        # return average
        minimum=min(salary)
        maximum=max(salary)
        average=(sum(salary)-maximum-minimum)/(len(salary)-2)
        return average
