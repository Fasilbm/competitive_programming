class Solution:
    def isValid(self, s: str) -> bool:
        self.stack=[]
        dict={'(':')','{':'}','[':']'}
        for i in s:
            if i == '(' or i=='[' or i=='{':
                self.stack.append(i)
            elif len(self.stack)==0 or i!=dict[self.stack.pop()]:
                     return False
        return len(self.stack)==0
        
        
        
