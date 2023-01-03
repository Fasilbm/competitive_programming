class Solution:
    def freqAlphabets(self, s: str) -> str:
        hash_map={}
        alpha=97
        answer=[]
        for i in range(1,27):
            hash_map[i]=chr(alpha)
            alpha+=1
        ptr=0
        while ptr<len(s):
            temp=[]
            if ptr<len(s)-2 and s[ptr+2]=="#":
            
                    temp.append(s[ptr])
                    temp.append(s[ptr+1])
                    ptr+=3
                    answer.append(hash_map[int("".join(temp))])
            else:
                answer.append(hash_map[int(s[ptr])])
                ptr+=1
        return "".join(answer
