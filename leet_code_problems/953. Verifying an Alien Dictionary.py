class Solution:
    # def compare(self, word1, word2):
    #     pass

    def isAlienSorted(self, words,order) -> bool:
        alphabet={}
        for indx,char in enumerate(order):
                alphabet[char]=indx
        for i in range(len(words)-1):
            wor1=words[i]
            wor2=words[i+1]
            for j in range(len(wor1)):
                if j==len(wor2):
                    return (False)
                elif alphabet[wor1[j]]>alphabet[wor2[j]]:
                    return (False)
                elif alphabet[wor1[j]]==alphabet[wor2[j]]:
                    continue
                else:
                    break
        return True

                
       
