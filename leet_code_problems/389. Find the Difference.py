class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        hashmap_s=Counter(s)
        hashmap_t=Counter(t)

        for i in t:
           if hashmap_t[i]!=hashmap_s[i]:
               return i
        return " "


    
