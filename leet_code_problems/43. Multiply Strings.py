class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1=len(num1)-1
        len2=len(num2)-1
        hash_map={}
        strings="0123456789"
        for i in range(len(strings)):
            hash_map[strings[i]]=i
        new_num1=0
        for i in num1:
            new_num1+=hash_map.get(i,0)*(10**len1)
            len1-=1
        new_num2=0
        for i in num2:
            new_num2+=hash_map.get(i,0)*(10**len2)
            len2-=1
        return str(new_num1*new_num2)
        
        
