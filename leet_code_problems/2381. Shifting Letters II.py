class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0 for i in range(len(s)+1)]
        t=[]
        for i in range(len(shifts)):
            j=(shifts[i][0])
            k=(shifts[i][1])
            if shifts[i][-1]==1:
                 prefix[j]+=1
            else:
                prefix[j]+=-1
    
            if shifts[i][-1]==1:
                prefix[k+1]+=-1
            else:
                prefix[k+1]+=1
        for i in range(1,len(prefix)):
             prefix[i]=prefix[i]+prefix[i-1]
        for i,c in enumerate(s):
              t.append(chr(((ord(c)-ord('a')+prefix[i])%26)+97))
        return "".join(t)
 
