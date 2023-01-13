class Solution:
    def commonChars(self, words):
        ans=[]
        hash_table={}
        for i in range(26):
            hash_table[i]=chr(97+i)

        alphabet=[[0]*26 for i in range(len(words))]
        offset=ord("a")
        for i in range(len(words)):
            for char in words[i]:
                ascii=ord(char)
                alphabet[i][ascii-offset]+=1

        for i in range(len(alphabet[0])):
            if alphabet[0][i]!=0:
                minimum=alphabet[0][i]
                for j in range(1,len(alphabet)):
                    minimum=min(minimum,alphabet[j][i])
                for k in range(minimum):
                    ans.append(hash_table[i])
        return ans

       
