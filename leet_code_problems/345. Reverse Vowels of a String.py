class Solution:
    def reverseVowels(self, s: str) -> str:
        string=list(s)
        lp=0
        rp=len(string)-1
        vowels="aeiouAEIOU"
        while lp<rp:
            if string[lp] in vowels and string[rp] in vowels:
                string[lp],string[rp]=string[rp],string[lp]
                lp+=1
                rp-=1
            elif string[lp] in vowels and string[rp] not in vowels:
                rp-=1
            elif string[lp] not in vowels and string[rp] in vowels:
                lp+=1
            else:
                rp-=1
                lp+=1
        return "".join(string)
    #Time complexity O(n)
    #Space complexity O(n)
    
