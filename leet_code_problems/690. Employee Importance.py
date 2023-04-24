"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adj_list={}

        for emp in employees:
            adj_list[emp.id]=emp
        self.res=0
        def dfs(id):
            # nonlocal res
            self.res+=adj_list[id].importance

            for children in adj_list[id].subordinates:
                dfs(children)
        dfs(id)

        return self.res


            
            
