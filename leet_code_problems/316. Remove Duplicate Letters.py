class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        freq=Counter(s)

        for i in s:

            if not stack:

                stack.append(i)

            elif (i not in stack) and ord(stack[-1])<ord(i):
                 
                stack.append(i)
                                                                            
            elif (i not in stack) and ord(stack[-1])>ord(i):

                while stack and (freq[stack[-1]]>0 and ord(stack[-1])>ord(i)):
                      
                      stack.pop()

                stack.append(i)  

            freq[i]-=1 
            

        return "".join(stack)

        
