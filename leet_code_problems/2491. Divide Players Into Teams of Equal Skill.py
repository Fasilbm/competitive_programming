class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        l=1
        r=len(skill)-2
        chemistry=skill[0]+skill[len(skill)-1]
        sum_of_chem=skill[0]*skill[len(skill)-1]
        
        while l<r:
            if skill[l]+skill[r]==chemistry:
                sum_of_chem+=skill[l]*skill[r]
                l+=1
                r-=1
            else:
                return -1
        return sum_of_chem
                



       
