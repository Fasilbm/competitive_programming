class Solution:
    def sortSentence(self, s: str) -> str:
        list1=s.split(" ")
        sentence=" "
        for i in range(len(list1)):
            cur_min=i
            for j in range(i+1,len(list1)):
                if list1[j][-1]<list1[cur_min][-1]:
                    cur_min=j
            list1[i],list1[cur_min]=list1[cur_min],list1[i]
            
            
        for k in range(len(list1)):
            sentence+=list1[k][:-1]+" "
        return sentence[1:-1]
        
        
            
