class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        s1hash=Counter(s1)

        for i in range(len(s2)):

            s2hash=Counter(s2[i:i+len(s1)])

            if s1hash==s2hash:

                return True

        return False
