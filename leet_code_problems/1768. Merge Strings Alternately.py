class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=[]
        first_ptr=0
        second_ptr=0
        while first_ptr<len(word1) and second_ptr<len(word2):
            merged.append(word1[first_ptr])
            merged.append(word2[second_ptr])
            first_ptr+=1
            second_ptr+=1
        while first_ptr<len(word1):
             merged.append(word1[first_ptr])
             first_ptr+=1
        while second_ptr<len(word2):
             merged.append(word2[second_ptr])
             second_ptr+=1
        return "".join(merged)


       

       
