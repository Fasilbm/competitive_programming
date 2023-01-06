class Solution:
    def printVertically(self, s: str) -> List[str]:
        splited=list(s.split(" "))
        vertical_words=[]
        longest_word=0
        for i in range(len(splited)):
                longest_word=max(len(splited[i]),longest_word)
        for i in range(longest_word):
            temp=[]
            for j in range(len(splited)) :
                if len(splited[j])-1<i:
                    temp.append(" ")
                else:
                    temp.append(splited[j][i])
            for k in range(len(temp)-1,-1,-1):
                if temp[k]==" ":
                    temp.pop()
                else:
                    break
            vertical_words.append("".join(temp))
        return vertical_words 
        
